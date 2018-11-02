#!/usr/bin/python
#-*- coding: UTF-8 -*-

from flask_wtf import Form
from wtforms import SubmitField, StringField,PasswordField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf import FlaskForm


class CaseListForm(Form):
    case = StringField('描述', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('操作')


#钻石充值
class DiamondForm(Form):
    diamond = StringField('充值钻石数量', validators=[DataRequired(), NumberRange(), Length(1,999999)])
    nike_name = StringField('用户昵称', validators=[DataRequired(), Length(1,64)])
    submit = SubmitField('提交')

#金币充值
class GoldForm(Form):
    gold = StringField('充值金币数量', validators=[DataRequired(), NumberRange(), Length(1, 999999)])
    nike_name = StringField('用户昵称', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')

#查询用户信息
class UserinfoForm(Form):
    nike_name = StringField('用户昵称', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')

#查询MTT房间号
class MTTinfoForm(Form):
    mtt_name = StringField('房间名', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')

#清除玩家的VIP身份
class UserVipCancelForm(Form):
    nike_name = StringField('用户昵称', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')

#查询玩家的VIP身份
class UserVipForm(Form):
    nike_name = StringField('用户昵称', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')

#查询房间号
class RoomIDForm(Form):
    room_name = StringField('房间名', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('提交')