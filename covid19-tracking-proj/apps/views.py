from flask import Blueprint, render_template, jsonify, redirect, url_for
from sqlalchemy import func, and_, not_, distinct
import spider
from datetime import datetime
from models import History, Details
from exts import db, usa
import time

bp = Blueprint('/covid', __name__)

@bp.route('/addhistory')
def addhistory():
    spider.updateHistory()
    return redirect(url_for('/covid.index'))

@bp.route('/addstatedetails')
def addstatedetails():
    spider.updateStateDetails()
    return redirect(url_for('/covid.index'))

@bp.route('/addlasteststatedetails')
def addlateststatedetails():
    spider.updateRecentStateDetails()
    return redirect(url_for('/covid.index'))

@bp.route('/addlatesthistory')
def addlatesthistory():
    spider.updateRecentHistory()
    return redirect(url_for('/covid.index'))


@bp.route('/', endpoint = 'index')
def hello_world():
    return render_template("main.html")

@bp.route("/time")
def get_time():
    return time.strftime("%Y{}%m{}%d{} %X").format('/', '/', '/')

@bp.route("/c1")
def get_c1_data():
    histories = History.query.order_by(History.ds.desc()).first()
    return jsonify({"confirm": str(round(histories.confirm/1000, 0)) + 'k',
                    "suspect": str(round(histories.suspect/1000, 0)) + 'k',
                    "heal": str(round(histories.heal/1000, 0)) + 'k',
                    "dead": str(round(histories.dead/1000, 0)) + 'k'
                    })


@bp.route("/c2")
def get_c2_data():
    mostRecent = Details.query.order_by(Details.update_time.desc()).first().update_time
    confirms = (db.session.query(Details.state, func.sum(Details.confirm)) 
                         .filter(and_(Details.update_time == mostRecent, not_(Details.state.in_(['AS', 'DC','GU', 'MP', 'PR', 'VI'])))) 
                         .group_by(Details.state)
                         .all())
    res = []
    for tup in confirms:
        res.append({"name":usa[tup[0]], "value":int(tup[1])})
    return jsonify({"data":res})


@bp.route("/l1")
def get_l1_data():
    histories = db.session.query(History).order_by(History.ds.desc()).all()
    days = [each.ds.strftime(r'%m-%d') for each in histories]
    confirms = [each.confirm if each.confirm is not None else 0 for each in histories]
    suspects = [each.suspect if each.suspect is not None else 0 for each in histories]
    heals = [each.heal if each.heal is not None else 0 for each in histories]
    deads = [each.dead if each.dead is not None else 0 for each in histories]
    return jsonify({"day":days[:150][::-1], "confirm": confirms[:150][::-1], "suspect": suspects[:150][::-1], "heal": heals[:150][::-1], "dead": deads[:150][::-1]})


@bp.route("/l2")
def get_l2_data():
    histories = History.query.order_by(History.ds.desc()).all()
    days = [each.ds.strftime(r'%m-%d') for each in histories]
    confirm_adds = [each.confirm_add if each.confirm_add is not None else 0 for each in histories]
    suspect_adds = [each.suspect_add if each.suspect_add is not None else 0 for each in histories]
    return jsonify({"day":days[:150][::-1], "confirm_add": confirm_adds[:150][::-1], "suspect_add": suspect_adds[:150][::-1]})


@bp.route("/r1")
def get_r1_data():
    mostRecent = Details.query.order_by(Details.update_time.desc()).first().update_time

    top5 = Details.query.filter(Details.update_time == mostRecent).order_by(-Details.confirm).limit(5)

    states = []
    confirms = []
    for tup in top5:
        states.append(usa[tup.state])
        confirms.append(tup.confirm)
    return jsonify({"state": states, "confirm": confirms})