В файле locators.py — используемые в тестах локаторы;

В файле conftest.py — используемые в тестах фикстуры;

В файле burger_constructor_data.py — hardcoded-значения из Конструктора бургеров.


Реализованные тесты:

test_registration.py
1. test_successful_registration — проверка успешной регистрации
2. test_try_to_registration_with_incorrectly_filled_fields — проверка регистрации с некорректно заполненными полями, вывод ошибки на некорректный пароль

test_login.py
1. test_successful_account_login_from_sign_in_button — проверка входа в ЛК через кнопку «Войти в аккаунт»
2. test_successful_account_login_from_private_office_button — проверка входа в ЛК через кнопку «Личный кабинет»
3. test_successful_account_login_from_sign_in_link_on_registration_form — проверка входа в ЛК через через ссылку «Войти» на форме регистрации
4. test_successful_account_login_from_sign_in_link_on_password_restore_form — проверка входа в ЛК через ссылку «Войти» на форме восстановления пароля

test_go_to_private_office.py
1. test_go_to_private_office_from_private_office_button — проверка перехода в ЛК через кнопку «Личный кабинет»

test_go_to_burger_constructor.py
1. test_go_to_burger_constructor_by_constructor_button_from_private_office — проверка перехода в конструктор по кнопке «Конструктор» из ЛК
2. test_go_to_burger_constructor_by_stellar_burgers_logo_from_private_office — проверка перехода в конструктор по логотипу в хэдере из ЛК

test_logout.py
1. test_logout_by_logout_button_from_private_office — выход из аккаунта по кнопке «Выйти» в профиле

test_burger_constructor.py
1. test_go_to_buns_section — проверка перехода к секции булок 
2. test_go_to_sauce_section — проверка перехода к секции соусов
3. test_go_to_stuffing_section — проверка перехода к секции начинок

