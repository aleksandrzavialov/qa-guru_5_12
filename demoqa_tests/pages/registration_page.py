from selene import be, have, command
from selene.support.shared import browser
from demoqa_tests import helpers, resource
from demoqa_tests.data.users import User


class RegistrationPage:
    def __init__(self):
        self.dropdown_menu = browser.all('[id^=react-select][id*=option]')

    def open(self):
        browser.open('/automation-practice-form')
        helpers.remove('#fixedban')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type('Ivan')
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, date):
        browser.element('#dateOfBirthInput').click()
        parsed_date = [date.strftime('%Y'), str(int(date.strftime('%m'))-1), date.strftime("%d")]
        browser.element(f'.react-datepicker__year-select [value="{parsed_date[0]}"]').click()
        browser.element(f'.react-datepicker__month-select [value="{parsed_date[1]}"]').click()
        browser.element(f'.react-datepicker__day--0{parsed_date[2]}:'
                        f'not(.react-datepicker__day--outside-month)').click()
        return self

    def _modal_should_have_registered_user_info(self, *args):
        browser.all(' td:nth-of-type(2)').should(have.exact_texts(args))

    def _select_subjects(self, value):
        for subject in value:
            browser.element('#subjectsInput').should(be.blank).type(subject).press_tab()
        return self

    def _select_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def _upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.get_path(value))
        return self

    def _fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def _select_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        self.dropdown_menu.element_by(have.exact_text(value)).click()
        return self

    def _select_city(self, value):
        browser.element('#city').perform(command.js.scroll_into_view).click()
        self.dropdown_menu.element_by(have.exact_text(value)).click()
        return self

    def _submit_data(self):
        browser.element('#submit').execute_script('element.click()')

    def _should_have_title(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))

    def _close_modal(self):
        browser.element('#closeLargeModal').should(be.clickable)

    def register(self, user: User):
        self.fill_first_name(user.first_name) \
            .fill_last_name(user.last_name) \
            .fill_email(user.email) \
            .select_gender(user.gender) \
            .fill_mobile(user.mobile) \
            .fill_date_of_birth(user.date_of_birth) \
            ._select_subjects(user.subjects) \
            ._select_hobby(user.hobby) \
            ._upload_picture(user.picture) \
            ._fill_address(user.address) \
            ._select_state(user.state) \
            ._select_city(user.city) \
            ._submit_data()

    def should_have_registered(self, user: User):
        self._should_have_title('Thanks for submitting the form')
        self._modal_should_have_registered_user_info(f'{user.first_name} {user.last_name}', user.email, user.gender,
                                                     user.mobile, user.date_of_birth.strftime('%d %B,%Y'),
                                                    ', '.join(user.subjects), user.hobby, user.picture, user.address,
                                                    f'{user.state} {user.city}')
        self._close_modal()