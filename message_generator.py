import datetime
import file_operation as file
import check_file


def make_massages(persons):
    now = datetime.datetime.now()
    for key, value in persons.items():
        text = f'{now.date()}, Gdynia\n\n\
        Welcome {value[0]} {value[1]},\n\n\
This is a kindly reminder that you have {value[2]}\n\
tasks left to submit before you can graduate.\n\n\
Your current grade is {value[3]} and can increase to {value[3]+1}\n\
if you submit all assignments in 1 month.\n\n\
        Socrates\n\
        Your teacher'
        save_to_file(key, text)


def save_to_file(file_name, content):
    check_file.do_this_with_file(f'{file_name}.txt', 'write', content)


def main():

    students = file.import_data('students.csv')
    make_massages(students)


if __name__ == '__main__':
    main()
