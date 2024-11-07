import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from helpers import retrieve_phone_code
from urban_routes_page import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        #CORRECCION Y CAMBIO DE CODIGO
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)
        WebDriverWait(cls.driver, 5).until(ec.visibility_of_element_located(cls.routes_page.from_field))

    def test_set_route(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    # CORRECCIÓN
    def test_select_comfort_tariff(self):
        self.routes_page.click_request_taxi()
        self.routes_page.select_comfort_tariff()
        active_tariff = self.routes_page.driver.find_element(*self.routes_page.active_tariff_container)
        tariff_title = active_tariff.find_element(*self.routes_page.tariff_title)
        assert tariff_title.text == "Comfort", "La tarifa Comfort no está seleccionada correctamente."

    def test_confirm_phone(self):
        self.routes_page.enter_phone_number(data.phone_number)
        confirmation_code = retrieve_phone_code(self.driver)
        self.routes_page.enter_confirmation_code(confirmation_code)
        phone_element = self.routes_page.driver.find_element(*self.routes_page.phone_number_text)
        assert phone_element.text == data.phone_number, f"El número de teléfono mostrado '{phone_element.text}' no coincide con el esperado '{data.phone_number}'."

    def test_add_credit_card(self):
        self.routes_page.add_credit_card(data.card_number, data.card_code)
        credit_card_element = self.routes_page.driver.find_element(*self.routes_page.credit_card_text)
        assert credit_card_element.text == "Tarjeta", f"El texto de la tarjeta '{credit_card_element.text}' no coincide con 'Tarjeta'."

    # CORRECCIÓN
    def test_message_for_driver(self):
        self.routes_page.write_message_for_driver(data.message_for_driver)
        comment_element = self.routes_page.driver.find_element(*self.routes_page.comment_input)
        assert comment_element.get_attribute("value") == data.message_for_driver, \
            f"El comentario '{comment_element.get_attribute('value')}' no coincide con '{data.message_for_driver}'."

    # CORRECCIÓN
    def test_request_blanket_and_tissues(self):
        self.routes_page.request_blanket_and_tissues()
        blanket_tissues_checkbox = self.routes_page.driver.find_element(*self.routes_page.request_blanket_tissues_checkbox)
        assert blanket_tissues_checkbox.is_selected(), "El checkbox de mantas y pañuelos no está seleccionado."

    # CORRECCIÓN
    def test_request_two_ice_creams(self):
        self.routes_page.request_two_ice_creams()
        counter_element = self.routes_page.driver.find_element(*self.routes_page.counter_value)
        assert counter_element.text == "2", f"El valor del contador es '{counter_element.text}', pero se esperaba '2'."

    # CORRECCIÓN
    def test_taxi_modal_appears(self):
        self.routes_page.click_reserve_button()
        self.routes_page.is_taxi_modal_visible()
        search_taxi_modal_element = self.routes_page.driver.find_element(*self.routes_page.search_taxi_modal)
        assert search_taxi_modal_element.is_displayed(), "El modal de búsqueda de taxi no está visible después de reservar el taxi."

    # CORRECCIÓN
    def test_driver_information_in_modal(self):
        self.routes_page.is_driver_info_visible_in_modal()
        driver_info_visible = self.routes_page.driver.find_element(*self.routes_page.driver_icon)
        assert driver_info_visible.is_displayed(), "La información del conductor no está visible en el modal."

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()