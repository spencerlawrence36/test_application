import requests, time

from flask import url_for, current_app
from flask_socketio import SocketIO
import app
from app import celery


@celery.task(bind=True)
def run_processing_task(self, app, user_text):
    print('Celery Function kicked off')

    time.sleep(3)
    user_text_reverse = user_text[::-1]

    #TODO Send POST Request with reversed text
    # results_url = url_for('main_bp.sql_query_results', _external=True)
    # requests.post(results_url)

    print('Task Completed')

    return 'Finished'


