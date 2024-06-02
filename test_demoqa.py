from selene import browser, have
import os


FIRSTNAME = "Ivan"
LASTNAME = "Petroff"
USEREMAIL = "ivan@petroff.com"
USERNUMBER = "0958877666"
DATEOFBIRTHINPUT = "12 Jun 2006"
SUBJECTSINPUT = "English"
UPLOADPICTURE = os.path.abspath("qa_guru.png")
CURRENTADDRESS = "Capital city, Liberty str, 17"


def test_registration_form():
    browser.open("/")

    browser.element(".text-center").should(have.text("Practice Form"))
    browser.element("#firstName").type(FIRSTNAME).press_enter()
    browser.element("#lastName").type(LASTNAME).press_enter()
    browser.element("#userEmail").type(USEREMAIL).press_enter()
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type(USERNUMBER).press_enter()
    browser.element("#dateOfBirthInput").type(DATEOFBIRTHINPUT).press_enter()
    browser.element("#subjectsInput").type(SUBJECTSINPUT).press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element("#uploadPicture").send_keys(UPLOADPICTURE)
    browser.element("#currentAddress").type(CURRENTADDRESS)
    browser.element("#submit").click()
