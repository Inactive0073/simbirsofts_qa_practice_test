from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import PracticeFormPageLocators as pfp_locators
from os import getcwd


class PracticeFormPage(BasePage):
    def should_be_form_is_present(self):
        assert self.is_element_present(*pfp_locators.FORM_NAME), f'Name is not present. {self.browser.current_url=}'
        assert self.is_element_present(
            *pfp_locators.FORM_LAST_NAME), f'Lastname is not present. {self.browser.current_url=}'
        assert self.is_element_present(*pfp_locators.FORM_EMAIL), f'Email is not present. {self.browser.current_url=}'
        assert self.is_element_present(*pfp_locators.FORM_GENDER), f'Gender is not present. {self.browser.current_url=}'
        assert self.is_element_present(*pfp_locators.FORM_PHONE), f'Phone is not present. {self.browser.current_url=}'
        assert self.is_element_present(
            *pfp_locators.FORM_DATE_BIRTHDAY), f'Date birthday is not present. {self.browser.current_url=}'
        assert self.is_element_present(
            *pfp_locators.FORM_SUBJECTS), f'Subjects is not present. {self.browser.current_url=}'
        assert self.is_element_present(
            *pfp_locators.FORM_HOBBIES), f'Hobbies is not present. {self.browser.current_url=}'
        assert self.is_element_present(
            *pfp_locators.FORM_PICTURE), f'Picture is not present. {self.browser.current_url=}'
        assert self.is_element_present(
            *pfp_locators.FORM_ADDRESS), f'Address is not present. {self.browser.current_url=}'
        assert self.is_element_present(*pfp_locators.FORM_STATE), f'State is not present. {self.browser.current_url=}'
        assert self.is_element_present(*pfp_locators.FORM_CITY), f'City is not present. {self.browser.current_url=}'

    def fill_and_send_form(self):
        self.fill_name_bar()
        self.fill_lastname_bar()
        self.fill_email_bar()
        self.select_gender()
        self.fill_phone_bar()
        self.select_birthday()
        self.fill_subjects_bar()
        self.select_hobby()
        self.send_pic()
        self.fill_address_bar()
        self.select_state_and_city()
        self.click_to_the_form_button()

    def fill_name_bar(self):
        self.name = self.browser.find_element(*pfp_locators.FORM_NAME)
        self.name.send_keys('Name')
        self.name = self.name.text
        print(self.name)

    def fill_lastname_bar(self):
        self.lastname = self.browser.find_element(*pfp_locators.FORM_LAST_NAME)
        self.lastname.send_keys('Lastname')
        self.lastname = self.lastname.text
        self.student_name = self.name + self.lastname
        print(self.student_name)

    def fill_email_bar(self):
        self.email = self.browser.find_element(*pfp_locators.FORM_EMAIL)
        self.email.send_keys('email@email.com')
        self.email = self.email.text
        print(self.email)

    def select_gender(self):
        gender_elements = self.browser.find_elements(*pfp_locators.FORM_GENDER_LABEL)
        self.gender = gender_elements[0]
        self.gender.click()
        self.selected_gender = self.get_selected_into_input_text(self.gender)
        print(self.selected_gender)

    def fill_phone_bar(self):
        self.phone = self.browser.find_element(*pfp_locators.FORM_PHONE)
        self.phone.send_keys('9991112233')
        self.phone = self.phone.text
        print(self.phone)

    def select_birthday(self):
        self.date_bar = self.browser.find_element(*pfp_locators.FORM_DATE_BIRTHDAY)
        self.date_bar.click()
        date_weeks = self.browser.find_elements(*pfp_locators.FORM_DATE_WEEKS)
        self.date = date_weeks[0].find_elements(*pfp_locators.FORM_DAYS)[0]
        self.date.click()
        self.date_bar = self.date_bar.get_attribute('value')
        print(self.date_bar)

    def fill_subjects_bar(self):
        self.browser.find_element(*pfp_locators.FORM_SUBJECTS).click()
        self.txt = 'something'
        self.browser.find_element(*pfp_locators.FORM_SUBJECTS_INPUT).send_keys(self.txt)

    def select_hobby(self):
        self.hobby = self.browser.find_elements(*pfp_locators.FORM_HOBBIES_LABEL)[0]
        self.hobby.click()
        self.hobby = self.get_selected_into_input_text(self.hobby)
        print(self.hobby)

    def send_pic(self):
        self.pic_file = 'image.jpg'
        self.browser.find_element(*pfp_locators.FORM_PICTURE).send_keys(f'{getcwd()}/{self.pic_file}')

    def fill_address_bar(self):
        self.address = self.browser.find_element(*pfp_locators.FORM_ADDRESS)
        self.address.send_keys('Ulyanovsk, Minaeva st.')
        self.address = self.address.text
        print(self.address)

    def select_state_and_city(self):
        self.browser.find_element(*pfp_locators.FORM_STATE).click()
        self.browser.find_elements(*pfp_locators.FORM_STATE_MENU)[0].click()
        self.browser.find_element(*pfp_locators.FORM_CITY).click()
        self.browser.find_elements(*pfp_locators.FORM_CITY_MENU)[0].click()
        self.state_and_city = self.browser.find_element(
            *pfp_locators.FORM_STATE_TEXT).text + ' ' + self.browser.find_element(*pfp_locators.FORM_CITY_TEXT).text
        print(self.state_and_city)

    def click_to_the_form_button(self):
        self.browser.find_element(*pfp_locators.FORM_BUTTON).click()

    def get_selected_into_input_text(self, elem):
        return self.browser.find_element(By.ID, elem.get_attribute('for')).get_attribute('value')

    def should_be_success_msg(self):
        assert self.browser.find_element(*pfp_locators.FORM_POPUP_SUCCESS_MSG).text == 'Thanks for submitting the form'

    def bars_should_be_the_same(self):
        # assert self.name =


        pass