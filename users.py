import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user, содержащую данные о пользователях
    """
    __tablename__ = 'user'

    id = sa.Column(sa.String(36), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def connect_db():
    """
    Устанавливает соединение к базе данных
    """

    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Здравствуйте! Пожалуйста, введите ваши данные!")
    first_name = input("Имя: ")
    last_name = input("Фамилию: ")
    gender = input("Ваш пол (варианты: Male, Female) ")
    email = input("Email: ")
    birthdate = input("Дата рождения в формате ГГГГ-ММ-ДД. Например, 1999-01-01: ")
    height = input("Рост в метрах? (Для разделения целой и десятичной части используйте точку)")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def main():
    """
    Обрабатывает пользовательский ввод
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Ваши данные сохранены. Спасибо!")


if __name__ == "__main__":
    main()