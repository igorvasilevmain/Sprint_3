from selenium.webdriver.common.by import By


class Locators:
    # Кнопка "Личный кабинет"
    PRIVATE_OFFICE_BUTTON = (By.XPATH, "//a[@href='/account']")
    # Кнопка "Войти в аккаунт"
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Поле ввода email на форме авторизации
    EMAIL_INPUT_FIELD_ON_AUTH_FORM = (By.XPATH, "//input[@name='name']")
    # Поле ввода пароля
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка "Войти" на форме авторизации
    SIGN_IN_BUTTON_ON_AUTH_FORM = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Зарегистрироваться" на форме авторизации
    REGISTRATION_LINK = (By.XPATH, "//a[@href='/register']")
    # Поле ввода имени на форме регистрации
    NAME_INPUT_FIELD = (By.XPATH, "//fieldset[1]//input[@name='name']")
    # Поле ввода email на форме регистрации
    EMAIL_INPUT_FIELD = (By.XPATH, "//fieldset[2]//input[@name='name']")
    # Кнопка "Зарегистрироваться" на форме регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ссылка "Войти" на форме регистрации
    SIGN_IN_LINK = (By.XPATH, "//a[@href='/login']")
    # Ссылка "Восстановить пароль" на форме авторизации
    PASSWORD_RESTORE_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    # Ошибка на неправильный пароль на форме регистрации
    INCORRECT_PASSWORD_ERROR = (
        By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    # Кнопка "Оформить заказ" на Главной
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Личный кабинет пользователя
    USER_PROFILE = (By.XPATH, "//a[@href='/account/profile']")
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # Кнопка "Конструктор" в хэдере
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Блок конструктора бургеров
    BURGER_CONSTRUCTOR = (
        By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")
    # Лого в хэдере
    STELLAR_BURGERG_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    # Секция булок в конструкторе бургеров
    BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")
    # Флюоресцентная булка R2-D3
    BUN = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    # Секция соусов в конструкторе бургеров
    SAUSE_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")
    # Соус с шипами Антарианского плоскоходца
    SAUCE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa75']")
    # Секция начинок в конструкторе бургеров
    STUFFING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")
    # Сыр с астероидной плесенью
    CHEESE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa7a']")
    # Модальное окно с выбранной позицией
    MODAL = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
