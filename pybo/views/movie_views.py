from flask import Blueprint, render_template, request

from pybo.forms import NaverBookForm
from pybo.movieapi import Mrank

bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/now/')
def Movienow():
    result= Mrank()
    return render_template('movie/movietop.html', movieinfo_toplist=result)

# SQL , NO-SQL

#SQL - MYSQL, 오라클 , 마리아DB, MS-SQL, SQLite
#NO-SQL - MONGODB, Redis, ......