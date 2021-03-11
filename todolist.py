from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

# Usado para criar a database
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# Classe base de onde objetos do SQL devem derivar
Base = declarative_base()


# Classe que define o database
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='task')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


def open_session():
    global engine
    Session = sessionmaker(bind=engine)
    session = Session()  # objeto utilizado para trabalhar com o database
    return session


def print_tasks():
    session = open_session()
    tasks = session.query(Table).all()
    if len(tasks) == 0:
        print("Nothing to do!\n")
    else:
        print(tasks)


def add_task():
    session = open_session()
    task_name = input("Enter task\n")
    new_row = Table(task=task_name,
                    deadline=datetime.today().date())
    session.add(new_row)  # adicionando nova coluna
    session.commit()  # comitando a mudanca
    print("The task has been added!\n")


def menu():
    while True:
        print("1) Today's tasks")
        print("2) Add task")
        print("0) Exit")
        option = int(input())

        if option == 1:
            print_tasks()
        elif option == 2:
            add_task()
        elif option == 0:
            print("Bye!")
            exit()
        else:
            print("Option not found!\n")


# Criando o database
Base.metadata.create_all(engine)

menu()
