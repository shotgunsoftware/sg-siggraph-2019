import datetime
import json
import os
from flask import Flask, request
import requests
import shotgun_api3

SITE_URL = os.environ.get('SG_HOST') + '/api/v1'
SCRIPT_NAME = os.environ.get('SG_SCRIPT_NAME')
SCRIPT_KEY = os.environ.get('SG_SCRIPT_KEY')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def ami_endpoint():
    delivery_count = process_shots()
    return "Processed %d deliveries" % delivery_count

def process_shots():
    delivery_count = 0
    auth_header = get_auth_header()
    for shot_id in [int(i) for i in request.form.get('selected_ids').split(',')]:
        versions = get_versions_for_shot(auth_header, shot_id)
        if versions:
            deliveries = create_delivery_with_versions(auth_header, versions)
            if deliveries:
                delivery_count += 1
    return delivery_count

def get_auth_header():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    params = {
        'client_id': SCRIPT_NAME,
        'client_secret': SCRIPT_KEY,
        'grant_type': 'client_credentials',
        'session_uuid': request.form.get('session_uuid')
    }
    resp = requests.post(SITE_URL + '/auth/access_token', headers=headers, params=params)

    return {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + resp.json()['access_token']
    }

def get_versions_for_shot(auth_header, shot_id):
    # Get all pndng versions for a shot
    headers = {
        'Content-Type': 'application/vnd+shotgun.api3_array+json'
    }
    headers.update(auth_header)
    filters = {
        'filters': [
            ['entity', 'is', {'type':'Shot', 'id':shot_id}],
            ['sg_status_list', 'is', 'pndng']
        ]
    }
    resp = requests.post(SITE_URL + '/entity/version/_search', headers=headers, data=json.dumps(filters))
    return resp.json().get('data')

def create_delivery_with_versions(auth_header, versions):
    headers = {
        'Content-Type': 'application/json'
    }
    headers.update(auth_header)
    data = {
        'title': datetime.datetime.now().strftime('%Y-%m-%d'),
        'sg_versions': [{'type': 'Version', 'id': version['id']} for version in versions],
        'project': {'type': 'Project', 'id': int(request.form['project_id'])}
    }
    resp = requests.post(SITE_URL + '/entity/delivery', headers=headers, data=json.dumps(data))
    return resp.json().get('data')

if __name__ == "__main__":
    app.run(debug=True)
