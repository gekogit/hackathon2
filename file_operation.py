def check_values(values):
    (nr_class, name, surname, work_to_do, grade) = tuple(values)
    name = correct_size_letter(name)
    surname = correct_size_letter(surname)
    if not check_class(nr_class):
        print(f"Błedny zapis klasy dla ucznia {name} {surname}")
    work_to_do = make_value(work_to_do, name, surname, 'work to do')
    grade = make_value(grade, name, surname, 'grade')
    return [nr_class, name, surname, work_to_do, grade]


def correct_size_letter(data_in):
    # check size first letter
    return data_in.capitalize()


def check_class(data_in):
    try:
        return data_in[1].isalpha() and data_in[0].isnumeric()
    except Exception:
        print("Brak lub niepełna nazwa klasy")
        exit(1)


def make_value(data_in, name, surname, task):
    try:
        return int(data_in)
    except Exception:
        print(f'Niepoprawna wartość w polu {task} dla ucznia {name} {surname}')
        exit(1)


def import_data(file_name):
    dict_student = {}
    try:
        with open(file_name, 'r') as f_open:
            content = (f_open.readlines())
            # Remove first description line
            content.pop(0)
            # Read line in file
            for line in content:
                # Remove endline sign
                line = line.strip('\n')
                # Split file value
                values = line.split(';')
                values = check_values(values)
                # Make dictionary from file value
                key_name = f"{values[0]}_{values[1]}_{values[2]}"
                values[3] = int(values[3])
                values[4] = int(values[4])
                dict_student[key_name] = values[1:]
            return dict_student
    except FileNotFoundError as err:
        print("Taki plik nie istnieje. Spróbuj wprowadzić ponownie nazwe pliku")


if __name__ == '__main__':
    filename = 'students.csv'
    print(import_data(filename))
