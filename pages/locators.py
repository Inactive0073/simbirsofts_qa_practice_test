from selenium.webdriver.common.by import By


class PracticeFormPageLocators:
    #FORM FIELDS
    FORM_NAME = (By.CSS_SELECTOR, '#firstName')
    FORM_LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    FORM_EMAIL = (By.ID, 'userEmail')
    FORM_GENDER = (By.CSS_SELECTOR, 'input[name="gender"]')
    FORM_GENDER_LABEL = (By.CSS_SELECTOR, 'input[name="gender"]+label')
    FORM_PHONE = (By.ID, 'userNumber')
    FORM_DATE_BIRTHDAY = (By.ID, 'dateOfBirthInput')
    FORM_DATE_WEEKS = (By.CLASS_NAME, 'react-datepicker__week')
    FORM_DAYS = (By.XPATH, '//div[@class="react-datepicker__week"]/div')
    FORM_SUBJECTS = (By.ID, 'subjectsInput')
    FORM_SUBJECTS_INPUT = (By.XPATH, '//input[@id="subjectsInput"]')
    FORM_HOBBIES = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    FORM_HOBBIES_LABEL = (By.CSS_SELECTOR, 'input[type="checkbox"] + label')
    FORM_PICTURE = (By.ID, 'uploadPicture')
    FORM_ADDRESS = (By.ID, 'currentAddress')
    
    FORM_STATE = (By.XPATH, '//div[@id="state"]')
    FORM_STATE_MENU = (By.XPATH, '//div[@id="state"]/div/div')
    FORM_STATE_TEXT = (By.XPATH, '//div[@tabindex]')
    
    FORM_CITY = (By.XPATH, '//div[@id="stateCity-wrapper"]/div[3]')
    FORM_CITY_MENU = (By.XPATH, '//div[@id="city"]/div/div')
    FORM_CITY_TEXT = (By.XPATH, '//div[@tabindex]')
    
    FORM_BUTTON = (By.CSS_SELECTOR, 'button#submit')

    #SUCCESS_FIELDS
    FORM_POPUP_SUCCESS_MSG = (By.ID, 'example-modal-sizes-title-lg')
    FORM_POPUP_STUDENT_NAME = (By.XPATH, '//td[contains(text(), "Student Name")]/following-sibling::td')
    FORM_POPUP_EMAIL = (By.XPATH, '//td[contains(text(), "Student Email")]/following-sibling::td')
    FORM_POPUP_GENDER = (By.XPATH, '//td[contains(text(), "Gender")]/following-sibling::td')
    FORM_POPUP_PHONE = (By.XPATH, '//td[contains(text(), "Mobile")]/following-sibling::td')
    FORM_POPUP_DATE_BIRTHDAY = (By.XPATH, '//td[contains(text(), "Date of Birth")]/following-sibling::td')
    FORM_POPUP_HOBBIES = (By.XPATH, '//td[contains(text(), "Hobbies")]/following-sibling::td')
    FORM_POPUP_PIC = (By.XPATH, '//td[contains(text(), "Picture")]/following-sibling::td')
    FORM_POPUP_ADDRESS = (By.XPATH, '//td[contains(text(), "Address")]/following-sibling::td')
    FORM_POPUP_STATE_AND_CITY = (By.XPATH, '//td[contains(text(), "State and City")]/following-sibling::td')
