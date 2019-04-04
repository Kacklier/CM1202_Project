#Author: Jamie
import csv

database = 'tests/results.csv'
tests = 'tests/tests.csv'

def save_result(student_id, student_name, test_id, test_type, result):
	'''
		--Example:
		save_result('1', 'Jamie', '1', 'summative', '75')
		-- Example end
	'''
	row = [student_id, student_name, test_id, test_type, result]

	try:
		with open(database, 'a', newline='') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(row)
		csvFile.close()
		print(f'Result has been saved for student id: {student_id}')
	except Exception as ex:
		print(ex)


def modify_result(student_id, test_type, new_result):
	'''
		--Example:
		modify_result('2', 'summative', '100')
		-- Example end
	'''
	row = ['', '', '', '', '']
	lines = ''

	with open(database, 'r') as readFile:
		reader = csv.reader(readFile)
		lines = list(reader)
	readFile.close()
	
	for line in lines:
		if line[0] == student_id and line[3] == test_type:
			row = line

	row[4] = new_result

	try:
		with open(database, 'w', newline='') as writeFile:
			writer = csv.writer(writeFile)
			writer.writerows(lines)
		writeFile.close()
		print(f'Result has been modified for student id: {student_id}')
	except Exception as ex:
		print(ex)	    

def show_all_results():
	with open(database, 'r') as readFile:
		reader = csv.reader(readFile)
		return list(reader)

def get_students_results(test_id, test_type):	
	'''
		--Example:
			GetAllStudents("1", "summative")
		Returns:
			[('George', '86'), ('Daniel', '84')]
		-- Example end
	'''
	studentArray = show_all_results()
	studentDict = []

	for student in studentArray:
		if test_type.lower() == "summative":
			if student[3].lower() == "summative" and student[2] == test_id:
				studentDict.append((student[1], student[4]))
			else:
				continue
		else:
			if student[3].lower() == "formative" and student[2] == test_id:
				studentDict.append((student[1], student[4]))
			else:
				continue
	return studentDict	

def get_student_result(student_name, test_type, test_id):	
	'''
		--Example:
			get_student_result("George", "summative", "1")
		Returns:
			('George', '86')
		-- Example end
	'''
	student = ('', '')
	data = get_students_results(test_id, test_type)

	for s in data:
		if s[0] == student_name:
			student = s
	return student

def GetTests(test_type):	
	'''
		--Example:
			GetTests("summative")
		Returns:
			[('1', 'summative'), ('2', 'summative')]
		-- Example end
	'''
	tests_data = []
	content = []

	with open(tests, 'r') as readFile:
		reader = csv.reader(readFile)
		tests_data = list(reader)

	for d in tests_data:
		if d[0].lower() == "test" or d[0].lower() == "type":
			content.append(d[1])

	temp = []
	pairs = [ ';'.join(x) for x in zip(content[0::2], content[1::2]) ]

	to_return = []

	for pair in pairs:
		t = pair.split(';')
		if t[1].lower() == test_type.lower():
			to_return.append((t[0], t[1]))

	return to_return

#print(get_student_result("Emima", "formative", "5"))	
