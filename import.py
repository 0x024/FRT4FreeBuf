# -*- coding:utf-8 -*-
import os
import sys
import json
import subprocess
from face import FaceAPI
from face import DBConnect

outer_id="0x024"
reload(sys)
sys.setdefaultencoding('utf8')
conn = DBConnect.dbconnect()
cur = conn.cursor()

if not os.path.exists("./data/log/face_import.log"):
	os.mknod('./data/log/face_import.log')

def creat_faceset():
	cur.execute("select face_token from face_data")
	result=FaceAPI.facesetcreate(outer_id='{}'.format(outer_id))
	column=cur.fetchall()
	a=zip(*column)
	a=list(a[0])
	for i in a:
		print("******************************************")
		with open('./data/log/face_import.log','r') as f:
			f=f.read()
		if i in f :
			print "{}:------Has Been Exist!".format(i)
		if i not in f:
			with open("./data/log/face_import.log",'a') as f:
				f.write(i)
			print i
			result=FaceAPI.facesetaddface(outer_id='{}'.format(outer_id),face_tokens=i)
			print result
def create_table():
	cur.execute("show tables")
	tables=cur.fetchall()
	a=zip(*tables)	
	if 'face_data' not in a[0]:
		cur.execute("create table face_data(stuID varchar(12),stuname varchar(12),face_token varchar(32),gender varchar(10),facequality float)")
		conn.commit()
		cur.execute("insert into face_data values(0,'None','None','None',0)")
		conn.commit()
def insert_data():
 	cur.execute("insert into face_data values(%s,'%s','%s','%s',%s)"%(stuID,stuname,face_token,gender,facequality))
	conn.commit()
def check_stuID(stuID):
	global face_token,gender,facequality
	cur.execute("select stuID from face_data")
	column=cur.fetchall()
	a=zip(*column)
	if stuID in a[0]:
		print "{}:------Has been Exist!".format(stuID)
	if stuID not in a[0]:
		result=FaceAPI.detect(image_file=imagedir)
		face_token=result["faces"][0]["face_token"]
		gender=result["faces"][0]["attributes"]["gender"]["value"]
		facequality=result["faces"][0]["attributes"]["facequality"]["value"]
		print"StuID：{}".format(stuID)
		print"StuName：{}".format(stuname)
		print"face_token：{}".format(face_token)
		print"gender：{}".format(gender)
		print"facequality：{}".format(facequality)
		insert_data()
def get_stuID_stuname(dir,topdown=True):
	global stuID,stuname,imagedir
	fileList = [] 
 	for root, dirs, files in os.walk(dir, topdown):
		for PicName in files:
			fileList.append(os.path.join(root,PicName)) 
		for f in sorted(fileList):
			imagedir=f
			temp=f.split('/')[3].split('.')
			stuID=temp[0]
			stuname=temp[1]
			print("******************************************")
			check_stuID(stuID)
def main():
	FaceAPI.facesetdelete(outer_id="{}".format(outer_id),check_empty=0)
	create_table()
	get_stuID_stuname('./data/face_import')
	cur.execute("delete from `face_data` where stuID=0;")
	conn.commit()
	creat_faceset()
	cur.close()
	conn.close()
if __name__ == '__main__':
	main()
	print "Have Done!"



	

