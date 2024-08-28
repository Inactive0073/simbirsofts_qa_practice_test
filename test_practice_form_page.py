from .pages.practice_form_page import PracticeFormPage

def test_guest_can_to_send_form(browser):
    link = 'https://demoqa.com/automation-practice-form'
    form_page = PracticeFormPage(browser, link)
    form_page.open()
    form_page.should_be_form_is_present()
    form_page.fill_and_send_form()
    form_page.should_be_success_msg()