from application.salary import out_salary
from db.people import out_db
import datetime


if __name__ == '__main__':
    out_salary()
    out_db()
    now = datetime.datetime.now()
    print(f'{now.strftime("%d-%m-%Y %H:%M:%S")} модули импортированы')
    input("")
