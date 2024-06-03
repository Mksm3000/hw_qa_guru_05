from selene import browser, command, have
import os


def test_registration_form():
    browser.open("automation-practice-form")

    browser.element(".text-center").should(have.text("Practice Form"))

    browser.element("#firstName").type("Ivan").press_enter()
    browser.element("#lastName").type("Petroff").press_enter()
    browser.element("#userEmail").type("ivan@petroff.com").press_enter()
    browser.element('[for="gender-radio-1"]').perform(command.js.click)
    browser.element("#userNumber").type("0958877666").press_enter()
    browser.element("#dateOfBirthInput").type("12 Jun 1986").press_enter()
    browser.element("#subjectsInput").type("English").press_enter()
    browser.element('[for="hobbies-checkbox-2"]').perform(command.js.click)
    browser.element("#uploadPicture").send_keys(os.path.abspath("qa_guru.png"))
    browser.element("#currentAddress").type("Capital city, Liberty str, 17")
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#react-select-4-input").type("Delhi").press_enter()
    browser.element("#submit").perform(command.js.click)
