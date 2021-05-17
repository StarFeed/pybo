from flask import Blueprint,render_template,url_for
from werkzeug.utils import redirect

from pybo.models import Question,Answer
from datetime import datetime
from pybo import db

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')