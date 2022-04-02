import datetime


def import_data():
    dict_student={}
    with open('students.csv', 'r') as fopen:
        content = (fopen.readlines())
        # Remove first description line
        content.pop(0)
        # Read line in file
        for line in content:
            # Remove endline sign
            line = line.strip('\n')
            # Split file value
            values=line.split(';',',')
            # Make dictionary from file value
            key_name=(f"{values[0]}_{values[1]}_{values[2]}")
            dict_student[key_name]=values
        return dict_student


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
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as file_massage:
        file_massage.write(content)


def main():

    #students = {'8a_Pawel_Kowalski': ['Pawel', 'Kowalski', 32, 2], '2b_Ida_Nowak': ['Ida', 'Nowak', 2, 4]}
    students = import_data()
    make_massages(students)


if __name__ == '__main__':
    main()
