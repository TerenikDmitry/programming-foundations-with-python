import os

def read_file(file_name):
	current_dir_path = os.path.dirname(os.path.abspath(__file__))
	file = open(current_dir_path + "\\" + file_name, "r")
	file_content = file.read()
	file.close()

	print(file_content)

read_file("check_curse_words_temp_clear_text.txt")