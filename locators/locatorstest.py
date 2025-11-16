
from selenium.webdriver.common.by import By


#Локаторы для тестирования
class LocatorsForTest:



    #Главная страница. Кнопка вход и регистрация
    log_and_reg_button =  (By.XPATH, '//button[text() = "Вход и регистрация"]')

    #Форма входа. Кнопка "Войти"
    login_button = (By.XPATH, '//button[text() = "Войти"]')

    #Форма входа. Кнопка "Нет аккаунта"
    without_acc_button = (By.XPATH, '//button[text() = "Нет аккаунта"]')

    #Форма регистрации. Поле "Введите Email"
    email_input = (By.XPATH, '//input[contains(text(), "Введите Email")]')

    #Форма регистрации. Поле "Пароль"
    password_input = (By.XPATH, '//input[contains(text(), "Пароль")]')

    #Форма регистрации. Поле "Повторите пароль"
    password_repit_input = (By.NAME, "submitPassword")

    #Форма регистрации. Ошибка поля "Введите Email"
    email_input_err = (By.XPATH, '//*[contains(text(), "Введите Email") and contains(@class, "input_inputError")]')

    #Форма регистрации. Ошибка поля "Пароль"
    password_input_err = (By.XPATH, '//*[contains(text(), "Пароль") and contains(@class, "input_inputError")]')

    #Форма регистрации. Ошибка поля "Повторите пароль"
    password_repit_input_err = (By.XPATH, '//*[contains(text(), "Повторите пароль") and contains(@class, "input_inputError")]')

    #Форма регистрации. Сообщение об ошибке
    err_message = (By.XPATH, '//span[text() = "Ошибка"]')

    #Форма регистрации. Кнопка "Создать аккаунт"
    create_acc_button = (By.XPATH, '//button[text() = "Создать аккаунт"]')

    #Главная страница. Аватар пользователя после регестрации
    user_avatar = (By.XPATH, '//button[@class = "circleSmall"]')

    #Главная страница. Имя пользователя после регестрации
    user_name = (By.XPATH, '//h3[@class = "profileText name"]')

    #Главная страница. Кнопка "Разместить объявление"
    place_an_ad_button = (By.XPATH, '//button[text() = "Разместить объявление"]')

    #Главная страница. Кнопка "Выйти"
    exit_button  = (By.XPATH, '//button[text() = "Выйти"]')

    #Страница "Новое объявление". Поле "Название"
    product_name_input  = (By.XPATH, '//input[@name = "name"]')

    #Страница "Новое объявление". Выпадашка "Категория"
    product_category_dropdown = (By.NAME, "category")
    product_category_dropdown_choose = (By.XPATH, '//span[text() = "Хобби"]')
    
    #Страница "Новое объявление". Выпадашка "Город"
    city_select_dropdown = (By.NAME, "city")
    city_select_dropdown_choose = (By.XPATH, '//span[text() = "Санкт-Петербург"]')
    
    #Страница "Новое объявление". Поле "Описание товара"
    product_description_input  = (By.NAME, "description")

    #Страница "Новое объявление". Поле "Стоимость"
    price_input = (By.NAME, "price")

    #Страница "Новое объявление". Radiobutton
    product_condition_new_radiobutton = (By.XPATH, '//radio[contains(text(), "Новый")]')
    product_condition_used_radiobutton = (By.XPATH, '//radio[contains(text(), "Б/У")]')
    
    #Страница "Новое объявление". Кнопка "Опубликовать"
    publish_button = (By.XPATH, '//button[text() = "Опубликовать"]')

    #Профиль
    profile_page_open = (By.XPATH, '//*[contains(@class, "profilePage")]')

    #Профиль. Есть созданное объявление
    user_ad_exist = (By.XPATH, '//*[contains(@class, "profilePage_gridAndPaginaton") and contains(@class, "card")]')

    # Модальное окно с заголовком "Чтобы разместить объявление, авторизуйтесь"
    message_window = By.XPATH, '//h1[@class="h1"]'

    