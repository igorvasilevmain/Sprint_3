from selenium.webdriver.common.by import By

class Locators():
    PRIVATE_OFFICE_BUTTON = (By.XPATH, "//a[@href='/account']") # Кнопка "Личный кабинет"
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    EMAIL_INPUT_FIELD_ON_AUTH_FORM = (By.XPATH, "//input[@name='name']") # Поле ввода email на форме авторизации
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='Пароль']") # Поле ввода пароля
    SIGN_IN_BUTTON_ON_AUTH_FORM = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти" на форме авторизации
    REGISTRATION_LINK = (By.XPATH, "//a[@href='/register']") # Ссылка "Зарегистрироваться" на форме авторизации
    NAME_INPUT_FIELD = (By.XPATH, "//fieldset[1]//input[@name='name']") # Поле ввода имени на форме регистрации
    EMAIL_INPUT_FIELD = (By.XPATH, "//fieldset[2]//input[@name='name']") # Поле ввода email на форме регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться" на форме регистрации
    SIGN_IN_LINK = (By.XPATH, "//a[@href='/login']") # Ссылка "Войти" на форме регистрации
    PASSWORD_RESTORE_LINK = (By.XPATH, "//a[@href='/forgot-password']") # Ссылка "Восстановить пароль" на форме авторизации
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]") # Ошибка на неправильный пароль на форме регистрации
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ" на Главной
    USER_PROFILE = (By.XPATH, "//a[@href='/account/profile']") # Личный кабинет пользователя
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход" в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]") # Кнопка "Конструктор" в хэдере
    BURGER_CONSTRUCTOR = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2") # Блок конструктора бургеров
    STELLAR_BURGERG_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Лого в хэдере
    BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]") # Секция булок в конструкторе бургеров
    BUN = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']") # Флюоресцентная булка R2-D3
    SAUSE_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]") # Секция соусов в конструкторе бургеров
    SAUCE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa75']") # Соус с шипами Антарианского плоскоходца
    STUFFING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]") # Секция начинок в конструкторе бургеров
    CHEESE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa7a']") # Сыр с астероидной плесенью
    MODAL = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']") # Модальное окно с выбранной позицией

