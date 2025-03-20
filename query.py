import faker.generator
from faker import Faker
import random
from unicodedata import digit

from application import init_app
from application.database import Users, db

app = init_app()

def create_faker_users():
    fake = Faker("en")
    Faker.seed(4321)
    user_list = []
    numbers_of_user = 50

    with app.app_context():
        for i in range(numbers_of_user):
            user = Users()
            user.name = fake.name()
            user.email = fake.email()
            user.password = fake.password()
            user.phone = fake.phone_number()
            user.address = fake.address()
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        create_faker_users()

        for p in Users.query.all():
            print(p.name, p.id)




