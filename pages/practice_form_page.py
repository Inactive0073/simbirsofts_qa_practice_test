import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
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
        self.name = 'Name'
        self.browser.find_element(*pfp_locators.FORM_NAME).send_keys(self.name)

    def fill_lastname_bar(self):
        self.lastname = 'Lastname'
        self.browser.find_element(*pfp_locators.FORM_LAST_NAME).send_keys(self.lastname)
        self.student_name = f'{self.name} {self.lastname}'

    def fill_email_bar(self):
        self.email = 'email@email.com'
        self.browser.find_element(*pfp_locators.FORM_EMAIL).send_keys(self.email)

    def select_gender(self):
        gender_elements = self.browser.find_elements(*pfp_locators.FORM_GENDER_LABEL)
        self.gender = gender_elements[0]
        self.gender.click()
        self.selected_gender = self.get_selected_into_input_text(self.gender)

    def fill_phone_bar(self):
        self.phone = '9991112233'
        self.browser.find_element(*pfp_locators.FORM_PHONE).send_keys(self.phone)

    def select_birthday(self):
        self.date_bar = self.browser.find_element(*pfp_locators.FORM_DATE_BIRTHDAY)
        self.date_bar.click()
        date_weeks = self.browser.find_elements(*pfp_locators.FORM_DATE_WEEKS)
        self.date = date_weeks[0].find_elements(*pfp_locators.FORM_DAYS)[0]
        self.date.click()
        day, month, year = self.date_bar.get_attribute('value').split()
        self.date_bar = f'{day} {month},{year}'

    def fill_subjects_bar(self):
        self.browser.find_element(*pfp_locators.FORM_SUBJECTS).click()
        self.txt = 'something'
        self.browser.find_element(*pfp_locators.FORM_SUBJECTS_INPUT).send_keys(self.txt)

    def select_hobby(self):
        self.hobby = self.browser.find_elements(*pfp_locators.FORM_HOBBIES_LABEL)[0]
        self.hobby.click()
        self.hobby = self.hobby.text

    def send_pic(self):
        self.pic_file = 'image.jpg'
        self.browser.find_element(*pfp_locators.FORM_PICTURE).send_keys(f'{getcwd()}/{self.pic_file}')

    def fill_address_bar(self):
        self.address = 'Ulyanovsk, Minaeva st.'
        self.browser.find_element(*pfp_locators.FORM_ADDRESS).send_keys(self.address)
        self.browser.execute_script('window.scrollTo(0,400);')

    def find_result_method(self, _locator):
        driver_methods = [EC.element_to_be_clickable, EC.presence_of_element_located, EC.visibility_of_element_located]
        for method in driver_methods:
            try:
                WebDriverWait(self.browser, 5).until(method(_locator)).click()
                break
            except (ElementClickInterceptedException, TimeoutException):
                continue

    def select_state_and_city(self):
        self.find_result_method(pfp_locators.FORM_STATE)
        self.find_result_method(pfp_locators.FORM_STATE_MENU)
        self.find_result_method(pfp_locators.FORM_CITY)
        self.find_result_method(pfp_locators.FORM_CITY_MENU)
        state = self.browser.find_element(*pfp_locators.FORM_STATE_TEXT).text
        city = self.browser.find_element(*pfp_locators.FORM_CITY_TEXT).text
        self.state_and_city = f'{state} {city}'

    def click_to_the_form_button(self):
        btn = self.browser.find_element(*pfp_locators.FORM_BUTTON)
        self.browser.execute_script('arguments[0].click();', btn)

    def get_selected_into_input_text(self, elem):
        return self.browser.find_element(By.ID, elem.get_attribute('for')).get_attribute('value')

    def should_be_success_msg(self):
        popup_msg = self.browser.find_element(
            *pfp_locators.FORM_POPUP_SUCCESS_MSG).text
        assert  popup_msg == 'Thanks for submitting the form', f'Success messsage not found, {popup_msg=}'

    def result_strings_should_be_the_same(self):
        assert self.student_name == self.browser.find_element(
            *pfp_locators.FORM_POPUP_STUDENT_NAME).text, f'Имена не совпадают{self.student_name=}'
        assert self.email == self.browser.find_element(
            *pfp_locators.FORM_POPUP_EMAIL).text, f'Email не совпадают{self.email=}'
        assert self.selected_gender == self.browser.find_element(
            *pfp_locators.FORM_POPUP_GENDER).text, f'Пол не совпадает{self.selected_gender=}'
        assert self.phone == self.browser.find_element(
            *pfp_locators.FORM_POPUP_PHONE).text, f'Телефон не совпадает{self.phone=}'
        day_month, year = self.browser.find_element(*pfp_locators.FORM_POPUP_DATE_BIRTHDAY).text.split(',')
        popup_birthday = f'{day_month[:-1]},{year}'
        assert self.date_bar == popup_birthday, f'Дата рождения не совпадает {self.date_bar=}'
        assert self.hobby == self.browser.find_element(
            *pfp_locators.FORM_POPUP_HOBBIES).text, f'Хоббии не совпадают{self.hobby=}'
        assert self.pic_file == self.browser.find_element(
            *pfp_locators.FORM_POPUP_PIC).text, f'Картинка не совпадает{self.pic_file=}'
        assert self.address == self.browser.find_element(
            *pfp_locators.FORM_POPUP_ADDRESS).text, f'Адрес не совпадает{self.address=}'
        popup_state_and_city = self.browser.find_element(*pfp_locators.FORM_POPUP_STATE_AND_CITY).text
        assert self.state_and_city == popup_state_and_city, f'Штат и город не совпадает{self.state_and_city=}, {popup_state_and_city=}'
