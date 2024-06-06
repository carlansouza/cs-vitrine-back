from src.modules.database.db_connection import SessionLocal
from src.models.users_model import User as UserModel
from src.models.cars_models import Car
from src.modules.user.service import pwd_context
from src.models.users_model import Role

def seed():
    session = SessionLocal()
    users_data = [
        {
            "name": "admin",
            "email": "admin@admin.com",
            "hashed_password": pwd_context.hash("admin"),
            "role": Role.ADMIN.value
        },
        {
            "name": "user1",
            "email": "user1@example.com",
            "hashed_password": pwd_context.hash("password1"),
            "role": Role.USER.value
        }
    ]
    
    for user_data in users_data:
        user = UserModel(**user_data)
        session.add(user)
    
    session.commit()
    
    print("Seeded admin user")

    cars = [
            Car(
                name="Model S",
                brand="Tesla",
                model="2021",
                price=479999,
                image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/20180630_Tesla_Model_S_70D_2015_midnight_blue_left_front.jpg/800px-20180630_Tesla_Model_S_70D_2015_midnight_blue_left_front.jpg?20180701133308",
                d_alt="Tesla Model S"
            ),
            Car(
                name="Mustang",
                brand="Ford",
                model="2020",
                price=255999,
                image="https://img.goodfon.com/wallpaper/nbig/b/87/ford-mustang-nfs-hero-car-119.webp",
                d_alt="Ford Mustang"
            ),
            Car(
                name="Model 3",
                brand="Tesla",
                model="2021",
                price=339999,
                image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Tesla_Model_3_%282023%29%2C_long_range%2C_Japan%2C_left-front.jpg/800px-Tesla_Model_3_%282023%29%2C_long_range%2C_Japan%2C_left-front.jpg?20230908152106",
                d_alt="Tesla Model 3"
            ),
            Car(
                name="Model X",
                brand="Tesla",
                model="2021",
                price=389999,
                image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Tesla_Model_X_100D_1X7A6737.jpg/800px-Tesla_Model_X_100D_1X7A6737.jpg?20230223160135",
                d_alt="Tesla Model X"
            ),
            Car(
                name="Gol",
                brand="Volkswagen",
                model="2021",
                price=59999,
                image="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Volkswagen_Gol_G8_in_Montevideo_%28cropped%29.jpg/800px-Volkswagen_Gol_G8_in_Montevideo_%28cropped%29.jpg?20210127154506",
                d_alt="Volkswagen Gol"
            ),
            Car(
                name="Onix",
                brand="Chevrolet",
                model="2021",
                price=64999,
                image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Chevrolet_Onix_%28second_generation%2C_front_view%29.jpg/800px-Chevrolet_Onix_%28second_generation%2C_front_view%29.jpg?20200627161621",
                d_alt="Chevrolet Onix"
            ),
            Car(
                name="HB20",
                brand="Hyundai",
                model="2021",
                price=61999,
                image="https://www.automaistv.com.br/wp-content/plugins/seox-image-magick/imagick_convert.php?width=768&height=461&format=.jpg&quality=91&imagick=/wp-content/uploads/2020/11/P_20201031_170728_edited-768x461.jpg",
                d_alt="Hyundai HB20"
            )
    ]
    
    session.bulk_save_objects(cars)
    session.commit()
    session.close()
    
    print("Seeded cars")
    
if __name__ == "__main__":
    seed()