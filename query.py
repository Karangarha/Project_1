"""Script to generate and insert fake user data into the database."""

from faker import Faker

from application import init_app
from application.database import Users, db

app = init_app()

def create_faker_users():
    """Generate and insert fake users into the database."""
    fake = Faker("en")
    Faker.seed(4321)
    user_list = []
    number_of_users = 50  # Fixed typo (numbers_of_user → number_of_users)

    with app.app_context():
        for _ in range(number_of_users):  # Removed unused variable `i`
            user = Users(
                name=fake.name(),
                email=fake.email(),
                password=fake.password(),
                phone=fake.phone_number(),
                address=fake.address(),
            )
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        create_faker_users()

        for user_instance in Users.query.all():
            print(user_instance.name, user_instance.id)
