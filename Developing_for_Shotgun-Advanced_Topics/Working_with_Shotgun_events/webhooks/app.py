import os
import logging

from shotgun_api3 import Shotgun
from flask import Flask, request, make_response

app = Flask(__name__)
sg = Shotgun(
    os.environ.get('SG_HOST'),
    os.environ.get('SG_SCRIPT_NAME'),
    os.environ.get('SG_SCRIPT_KEY')
)

@app.route('/task_status', methods=['POST'])
def task_status():
    try:
        data = request.get_json()
        event = data['data']
        sg.set_session_uuid(event['session_uuid'])
        process_task_status_event(event)
    except Exception, e:
        return make_response(e.message, 500, {})
    return "Ok" # status 200

def process_task_status_event(event):
    if event['meta']['new_value'] == 'fin':
        downstream_tasks = sg.find(
            'Task',
            [['upstream_tasks', 'is', event['entity']]],
            ['sg_status_list']
        )
        batch_updates = [
            {
                "request_type": "update",
                "entity_type": "Task",
                "entity_id": task['id'],
                "data": {
                    "sg_status_list": 'rdy'
                }
            } for task in downstream_tasks
            if task['sg_status_list'] == 'wtg'
        ]
        sg.batch(batch_updates)
