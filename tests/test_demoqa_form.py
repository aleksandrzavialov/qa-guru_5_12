import datetime
import allure
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User, UserHobby, UserGender


@allure.title('Successful registration in demo QA')
def test_form_filling(browser_actions):
    registration_page = RegistrationPage()
    tested_user = User(first_name='Ivan', last_name='Petrov', email='ivanpetrov@mail.ru', gender=UserGender.Male.name,
                       mobile='8999999999', date_of_birth=datetime.date(1989, 11, 19), subjects=['Maths', 'Hindi'],
                       hobby=UserHobby.Reading.name, picture='Capibara.jpg',
                       address='Pushkina Street, Kolotushkina house',
                       state='Uttar Pradesh', city='Merrut')

    with allure.step('Open demo QA page'):
        registration_page.open()

    with allure.step('Fill registration information'):
        registration_page.register(tested_user)

    with allure.step("Check registration results"):
        registration_page.should_have_registered(tested_user)


