import os
import requests

def check_curse_word(text):
	request =  requests.get('http://www.wdylike.appspot.com', params = {'q':text})

	return request.json()

def read_file(file_name):
	print("read file: " + file_name)

	current_dir_path = os.path.dirname(os.path.abspath(__file__))
	file = open(current_dir_path + "\\" + file_name, "r")
	file_content = file.read()
	file.close()

	if check_curse_word(file_content):
		print("Some shite!")
	else:
		print("All good!")


read_file("check_curse_words_temp_clear_text.txt")
read_file("check_curse_words_temp_notclear_text.txt")