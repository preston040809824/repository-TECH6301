count = 0
with open('grades.txt', 'w') as grades:
    grades.write('Subject and Grades:')

   grades.write('\n')

while count < 12:
    subject = input(' Enter subject name: ')
    try:
        average = int(input('Enter grade average: '))
        if not 0 <= average <= 100:
            print('Average must be between 0 and 100')
            continue
    except ValueError:
        print('Input grade must be a number')
        continue

    with open('grades.txt', 'a') as grades:
        grades.write('Subject name: ')
        grades.write(subject)
        grades.write(' -- Student average grade: ')
        grades.write(str(average))
        grades.write('\n')

    count += 1

try:
    question = input('Enter file name for grades: ')
    if question == 'grades.txt':
        with open('grades.txt', 'r') as grades:
            grades_read = grades.read()
            print(grades_read)
except FileNotFoundError:
    print('File not found')