import os
import logging


def registerCallbacks(reg):
    """
    Register all necessary or appropriate callbacks for this plugin.
    """

    # Register a callback to into the event processing system.
    #
    # Arguments:
    # - Shotgun script name
    # - Shotgun script key
    # - Callable
    # - A filter to match events to so the callable is only invoked when
    #   appropriate
    # - Argument to pass through to the callable
    #

    eventFilter = {'Shotgun_Task_Change': ['sg_status_list']}
    reg.registerCallback(
        os.environ["SGDAEMON_TASKSTATUS_NAME"],
        os.environ["SGDAEMON_TASKSTATUS_KEY"],
        taskStatusFlipper,
        eventFilter,
        None,
    )

    reg.logger.setLevel(logging.DEBUG)


def taskStatusFlipper(sg, logger, event, args):
    """
    A callback that updates the task status.

    :param sg: Shotgun API handle.
    :param logger: Logger instance.
    :param event: A Shotgun EventLogEntry entity dictionary.
    :param args: Any additional misc arguments passed through this plugin.
    """
    if event['meta']['new_value'] == 'fin':
        downstream_tasks = sg.find('Task', [['upstream_tasks', 'is', event['entity']]], ['sg_status_list'])
        batch_updates = []
        for task in downstream_tasks:
            if task['sg_status_list'] == 'wtg':
                batch_updates.append(
                    {
                        "request_type": "update",
                        "entity_type": "Task",
                        "entity_id": task['id'],
                        "data": {
                            "sg_status_list": 'rdy'
                        }
                    }
                )
        sg.batch(batch_updates)
