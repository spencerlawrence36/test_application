import requests, json, time
from flask import render_template, request, url_for, current_app
from flask_socketio import send

from app import socketio
from app.main import main_bp
from app.main.forms import UserTextForm
from app.celery_tasks import run_processing_task

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = UserTextForm()
    if request.method == 'POST':
        request_data = request.form.to_dict()

        user_text = request_data['user_text']
        print(request_data['socket_id'])

        run_processing_task.apply_async(args=[user_text])

    return render_template('index.html', form=form)


@main_bp.route('/reversed_text_results', methods=['POST'])
def reversed_text_results():
    # TODO Send reversed text to Client via websocket

    return None

# @socketio.on('my_event')
# def user_test_task_results(my_event):
#     # Sends data to client
#     send(my_event, broadcast=True)

