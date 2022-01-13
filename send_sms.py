import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import pandas as pd
from random import randrange
import sys 

def choose_workouts():

	df = pd.read_csv('workout_options.txt')

	df = df.drop(df.columns[0],axis=1)
	# print(df)

	day = df.sample(1,axis=1)
	

	workout_list = day.iloc[:,0].tolist()
	cleaned_list = [x for x in workout_list if str(x) != 'nan']
	
	return cleaned_list


def send_text(cleaned_list):
	# carriers = ['@txt.att.net','@pm.sprint.com','@tmomail.net','@vtext.com']

	# for i in range(len(carriers)):

	# 	try:
	# 		email = "drewhahn23@gmail.com"
	# 		pas = "zjmxdfqrswjajkvx"





	sms_gateway = '9737148343@vtext.com'
	smtp = "smtp.gmail.com"
	port = 587
	server = smtplib.SMTP(smtp,port)
	server.starttls()
	server.login(email,pas)

	# message_text = 'hi'
	message_text = ''
	for i in cleaned_list:
		message_text += i
		message_text += '\n'
	msg = MIMEText(message_text)
	# msg['Subject'] = 'test'
	# msg['From'] = 'drew'
	msg['From'] = 'Drew <drewhahn23@gmail.com>'
	msg['To'] = sms_gateway
	msg['Date'] = formatdate(localtime=True)

	server.send_message(msg)

	server.quit()





if __name__ == '__main__':
	workouts = choose_workouts()
	send_text(workouts)

