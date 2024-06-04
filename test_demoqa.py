from selene import browser, command, have
import os


def test_registration_form():

    browser.open("automation-practice-form")

    browser.element(".text-center").should(have.text("Practice Form"))

    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Petroff")
    browser.element("#userEmail").type("ivan@petroff.com")
    browser.element("#userNumber").type("0958877666")

    browser.element('[for="gender-radio-1"]').click()

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select option").click()
    browser.element('[value="3"]').click()
    browser.element(".react-datepicker__year-select option").click()
    browser.element('[value="1984"]').click()
    browser.all(".react-datepicker__day--012").first.click()

    browser.element("#subjectsInput").type("Ph").press_tab()
    browser.element("#subjectsInput").type("Ma").press_tab()

    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element("#uploadPicture").send_keys(os.path.abspath("qa_guru.png"))

    browser.element("#currentAddress").type("Capital city, Liberty str, 17")

    browser.element("#state").click().element("#react-select-3-option-1").click()
    browser.element("#city").click().element("#react-select-4-option-1").click()

    browser.element("#submit").with_(timeout=5).press_enter()

    browser.element(".modal-content").element("table").all("tr").all("td").even.should(
        have.exact_texts(
            "Ivan Petroff",
            "ivan@petroff.com",
            "Male",
            "0958877666",
            "12 April,1984",
            "Physics, Maths",
            "Reading",
            "qa_guru.png",
            "Capital city, Liberty str, 17",
            "Uttar Pradesh Lucknow",
        )
    )
