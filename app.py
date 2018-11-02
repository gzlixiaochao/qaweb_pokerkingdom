#!/usr/bin/python
#-*- coding: UTF-8 -*-

from flask import Flask, render_template, redirect, url_for, request, flash
from forms import CaseListForm, DiamondForm, GoldForm, UserinfoForm, UserVipCancelForm, UserVipForm, MTTinfoForm, RoomIDForm
from flask_bootstrap import Bootstrap
from flask_login import login_required, login_user, logout_user, current_user
from ext import db, login_manager
import pymysql



SECRET_KEY = 'This is my key'

CASE_LISTS = [
    '钻石充值',
    '金币充值',
    '查询用户信息',
    '查询MTT房间信息',
    '清除玩家的VIP身份',
    '查询玩家的VIP身份',
    '查询房间信息',
]

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = SECRET_KEY
#
# HOST = '192.168.0.88'
# PORT = 3306
# USER = 'test'
# PASSWORD = '123456'
# DB = 'todolist'


HOST = '13.250.3.88'
PORT = 3306
USER = 'work'
PASSWORD = 'SqL0301myT2016est'
DB = 'dzpk'



# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://work:SqL0301myT2016est@13.250.3.88/dzpk"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# db_engine = sqlalchemy.create_engine("mysql+pymysql://work:SqL0301myT2016est@13.250.3.88/dzpk",
#                                      encoding='utf-8',
#                                      echo=True)


#
diamondrecharge_sql = "UPDATE user_money_account s set s.IDOU = {diamond}  where s.USER_ID =" \
                  " (select t.USER_ID from user_details_info t where t.nike_name = \'{nike_name}\')"

goldrecharge_sql = "UPDATE  user_details_info s set s.CHIP = {gold} WHERE nike_name = \'{nike_name}\'"

userinfo_sql = "select * from user_details_info t where t.nike_name= \'{nike_name}\'"

mttinfo_sql = "SELECT * from mtt_record t where t.mtt_name = \'{mtt_name}\'"

clearvip_sql = "DELETE FROM user_vip where user_id in (select USER_ID from user_details_info WHERE nike_name = \'{nike_name}\')"

vipinfo_sql = "SELECT * FROM user_vip WHERE USER_ID IN (SELECT USER_ID from user_details_info WHERE nike_name = \'{nike_name}\')"

roomnum_sql = "SELECT * from group_room where name = \'{name}\'"

sql1 = "select * from user_details_info t where t.nike_name= '李晓超004'"

def sql_exe_updata(sql):
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset='utf8')
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
    except pymysql.Error as e:
        return e
    finally:
        if conn is not None:
            conn.close()


def sql_exe_search(sql):
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset='utf8')
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    except pymysql.Error as e:
        return e
    finally:
        if conn is not None:
            conn.close()



@app.route('/')
def show_case_list():
    form = CaseListForm()
    return render_template('index.html', caselist=CASE_LISTS, form=form)

@app.route('/edit_diamond/', methods=['GET', 'POST'])
def edit_diamond():
    if request.method == 'GET':
        form = DiamondForm()
        return render_template('modify.html', form=form)
    else:
        form = DiamondForm()
        if form.validate_on_submit():
            diamond = request.form['diamond']
            nike_name = request.form['nike_name']
            sql = diamondrecharge_sql.format(diamond=diamond, nike_name=nike_name)
            # print(sql)
            sql_exe_updata(sql)
            flash("操作成功!")
        else:
            flash(form.errors)
        return redirect(url_for('show_case_list'))

@app.route('/edit_gold/', methods=['GET', 'POST'])
def edit_gold():
    if request.method == 'GET':
        form = GoldForm()
        return render_template('modify.html', form=form)
    else:
        form = GoldForm()
        if form.validate_on_submit():
            gold = request.form['gold']
            nike_name = request.form['nike_name']
            sql = goldrecharge_sql.format(gold=gold, nike_name=nike_name)
            # print(sql)
            sql_exe_updata(sql)
            flash("操作成功!")
        else:
            flash(form.errors)
        return redirect(url_for('show_case_list'))

@app.route('/show_user_info/', methods=['GET', 'POST'])
def show_user_info():
    if request.method == 'GET':
        form = UserinfoForm()
        return render_template('modify.html', form=form)
    else:
        form = UserinfoForm()
        if form.validate_on_submit():
            nike_name = request.form['nike_name']
            sql = userinfo_sql.format(nike_name=nike_name)
            # print(sql)
            result = sql_exe_search(sql)
            flash("操作成功!")
            flash(result)
        else:
            flash(form.errors)
        return redirect(url_for('show_case_list'))



@app.route('/show_mtt_info/', methods=['GET', 'POST'])
def show_mtt_info():
    if request.method == 'GET':
        form = MTTinfoForm()
        return render_template('modify.html', form=form)
    else:
        form = MTTinfoForm()
        if form.validate_on_submit():
            mtt_name = request.form['mtt_name']
            sql = mttinfo_sql.format(mtt_name=mtt_name)
            # print(sql)
            result = sql_exe_search(sql)
            flash("操作成功!")
            flash(result)
        else:
            flash(form.errors)
        return redirect(url_for('show_case_list'))


@app.route('/vip_cancel/', methods=['GET', 'POST'])
def vip_cancel():
    if request.method == 'GET':
        form = UserVipCancelForm()
        return render_template('modify.html', form=form)
    else:
        form = UserVipCancelForm()
        if form.validate_on_submit():
            nike_name = request.form['nike_name']
            sql = clearvip_sql.format(nike_name=nike_name)
            # print(sql)
            sql_exe_updata(sql)
            flash("操作成功!")
        else:
            flash(form.errors)
        return redirect(url_for('show_case_list'))


@app.route('/show_vip_info/', methods=['GET', 'POST'])
def show_vip_info():
    if request.method == 'GET':
        form = UserVipForm()
        return render_template('modify.html', form=form)
    else:
        form = UserVipForm()
        if form.validate_on_submit():
            nike_name = request.form['nike_name']
            sql = vipinfo_sql.format(nike_name=nike_name)
            # print(sql)
            result = sql_exe_search(sql)
            flash("操作成功!")
            flash(result)
        else:
            flash(form.errors)
        return redirect(url_for('show_case_list'))



@app.route('/show_room_info/', methods=['GET', 'POST'])
def show_room_info():
    if request.method == 'GET':
        form = RoomIDForm()
        return render_template('modify.html', form=form)
    else:
        form = RoomIDForm()
        if form.validate_on_submit():
            room_name = request.form['room_name']
            sql = roomnum_sql.format(room_name=room_name)
            # print(sql)
            result = sql_exe_search(sql)
            flash("操作成功!")
            flash(result)
        else:
            flash(form.errors)
        return redirect(url_for('show_case_list'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

