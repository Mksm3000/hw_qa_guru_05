from selene import browser, command, have
import os


def test_registration_form():

    # открываем страницу для тестирования
    browser.open("automation-practice-form")

    # проверяем что открыта страница с необходмым текстом
    browser.element(".text-center").should(have.text("Practice Form"))

    # вводим данные пользователя в виде текста
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Petroff")
    browser.element("#userEmail").type("ivan@petroff.com")
    browser.element("#userNumber").type("0958877666")

    # выбираем гендер при помощи клика на один из вариантов
    browser.element('[for="gender-radio-1"]').perform(command.js.click)

    # вводим дату выбирая предложенные год, месяц и дату
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select option").click()
    browser.element('[value="3"]').click()
    browser.element(".react-datepicker__year-select option").click()
    browser.element('[value="1984"]').click()
    browser.all(".react-datepicker__day--012").first.click()

    # вводим названия предметов и выбираем из списка
    browser.element("#subjectsInput").type("Ph").press_tab()
    browser.element("#subjectsInput").type("Ma").press_tab()

    # выбираем хобби при помощи клика на необходимые варианты
    browser.element('[for="hobbies-checkbox-2"]').perform(command.js.click)

    # загрузка изображения
    browser.element("#uploadPicture").send_keys(os.path.abspath("qa_guru.png"))

    # ввод адреса
    browser.element("#currentAddress").type("Capital city, Liberty str, 17")

    # вводим сначала название штата, затем название города
    browser.element("#state").click().element("#react-select-3-option-1").click()
    browser.element("#city").click().element("#react-select-4-option-1").click()

    # подтверждение заполнения формы
    browser.element("#submit").perform(command.js.click)
