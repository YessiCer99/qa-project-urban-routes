from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    comfort_tariff = (By.XPATH, '//*[text()="Comfort"]')
    active_tariff_container = (By.CSS_SELECTOR, '.tcard.active')  # Contenedor activo de la tarifa seleccionada
    tariff_title = (By.CLASS_NAME, 'tcard-title')  # Título de la tarifa dentro del contenedor activo
    phone_button = (By.CLASS_NAME, 'np-button')  # Botón para abrir el modal de teléfono
    phone_input = (By.ID, 'phone')  # Campo de entrada del número de teléfono
    next_button = (By.XPATH, '//*[text()= "Siguiente"]')
    confirmation_code_input = (By.ID, 'code')  # Localizador para el campo de código de confirmación
    confirm_button = (By.XPATH, '//button[text()="Confirmar"]')  # Localizador para el botón de "Confirmar"
    phone_number_text = (By.CLASS_NAME, 'np-text')
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.XPATH, '//*[text()="Agregar tarjeta"]')
    card_number_input = (By.ID, 'number')  # Campo para el número de la tarjeta
    card_code_input = (By.XPATH, '//div[@class="card-code-input"]//input[@id="code"]') #localizador del campo de código CVV
    modal_unusual = (By.CLASS_NAME, 'modal.unusual')  # Para hacer clic fuera del campo CVV
    add_card_submit_button = (By.XPATH, '//button[text()="Agregar"]')  # Botón para agregar la tarjeta
    close_payment_modal_button = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button') # localizador para cerrar la ventana de método de pago
    credit_card_text = (By.CLASS_NAME, 'pp-value-text')
    comment_input = (By.ID, 'comment') # Localizador del campo de comentario
    #request_blanket_tissues_checkbox = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > span') # Localizador del checkbox para pedir manta y pañuelos
    request_blanket_tissues_checkbox = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    request_ice_cream_plus_button = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus') # Localizador del botón + para pedir helados
    counter_value = (By.CSS_SELECTOR, 'div.counter-value')  # Localizador para el contador de clics
    reserve_button = (By.CSS_SELECTOR, 'button.smart-button') # Localizador para el botón "Reservar"
    search_taxi_modal = (By.CLASS_NAME, 'order-body')
    driver_icon = (By.XPATH, '//img[@src="/static/media/bender.e90e5089.svg"]') # Localizador una vez se muestra la información del conductor


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Método para hacer clic en "Pedir un taxi
    def click_request_taxi(self):
        taxi_button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.request_taxi_button))
        taxi_button.click()

    # Método para seleccionar la tarifa Comfort
    def select_comfort_tariff(self):
        comfort_button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.comfort_tariff))
        comfort_button.click()

        # Método para ingresar el numero de télefono
    def enter_phone_number(self, phone_number):
        # Hacer clic en el botón que abre la ventana para ingresar el teléfono
        phone_button_element = self.wait.until(ec.element_to_be_clickable(self.phone_button))
        phone_button_element.click()
        # Ingresar el número de teléfono en el campo correspondiente
        phone_input_element = self.wait.until(ec.element_to_be_clickable(self.phone_input))
        phone_input_element.send_keys(phone_number)
        # Hacer clic en el botón "Siguiente"
        next_button_element = self.wait.until(ec.element_to_be_clickable(self.next_button))
        next_button_element.click()

    # Método para ingresar el código de confirmación
    def enter_confirmation_code(self, code):
        confirmation_input = self.wait.until(ec.element_to_be_clickable(self.confirmation_code_input))
        confirmation_input.send_keys(code)
        # Hacer clic en el botón "Confirmar"
        confirm_button_element = self.wait.until(ec.element_to_be_clickable(self.confirm_button))
        confirm_button_element.click()

    # Método para agregar la tarjeta de crédito
    def add_credit_card(self, card_number, card_code):
        # Hacer clic en el botón Método de pago
        self.wait.until(ec.element_to_be_clickable(self.payment_method_button)).click()
        # Hacer clic en "Agregar tarjeta"
        self.wait.until(ec.element_to_be_clickable(self.add_card_button)).click()
        # Ingresar el número de tarjeta
        card_number_input_element = self.wait.until(ec.element_to_be_clickable(self.card_number_input))
        card_number_input_element.send_keys(card_number)
        # Ingresar el código CVV
        card_code_input_element = self.wait.until(ec.element_to_be_clickable(self.card_code_input))
        card_code_input_element.send_keys(card_code)
        # Cambiar el enfoque haciendo clic en otro lugar
        modal_unusual_element = self.wait.until(ec.element_to_be_clickable(self.modal_unusual))
        modal_unusual_element.click()  # Hacemos clic fuera del campo de CVV para perder el enfoque
        # Hacer clic en el botón "Agregar"
        add_card_submit_button_element = self.wait.until(ec.element_to_be_clickable(self.add_card_submit_button))
        add_card_submit_button_element.click()
        # Cerrar la ventana modal de pago
        close_payment_modal_button_element = self.wait.until(ec.element_to_be_clickable(self.close_payment_modal_button))
        close_payment_modal_button_element.click()

    # Método para escribir un mensaje para el controlador
    def write_message_for_driver(self, message):
        # Desplazarse al campo de comentario
        comment_input_element = self.driver.find_element(*self.comment_input)
        self.driver.execute_script("arguments[0].scrollIntoView();", comment_input_element)
        # Esperar a que el campo sea visible y escribir el mensaje
        comment_input_element = self.wait.until(ec.element_to_be_clickable(self.comment_input))
        comment_input_element.send_keys(message)

    # Método para seleccionar la opción de pedir manta y pañuelos
    def request_blanket_and_tissues(self):
        # Localizar el checkbox de manta y pañuelos
        blanket_tissues_checkbox = self.driver.find_element(*self.request_blanket_tissues_checkbox)
        # Hacer clic en el checkbox
        blanket_tissues_checkbox.click()

    # Método para pedir 2 helados
    def request_two_ice_creams(self):
        # Desplazar la página para visualizar el contador de helados
        ice_cream_plus_button = self.wait.until(ec.element_to_be_clickable(self.request_ice_cream_plus_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ice_cream_plus_button)
        # Hacer clic en el botón + dos veces
        ice_cream_plus_button.click()  # Primer clic
        ice_cream_plus_button.click()  # Segundo clic

    # Método para hacer clic en el botón Reservar
    def click_reserve_button(self):
        self.driver.find_element(*self.reserve_button).click()

    #Método para esperar a que aparezca la información del conductor
    def is_taxi_modal_visible(self):
        # Esperar hasta que aparezca el modal de búsqueda del taxi
        self.wait.until(ec.visibility_of_element_located(self.search_taxi_modal))

    def is_driver_info_visible_in_modal(self):
        # Esperar hasta que aparezca el ícono del conductor (25 segundos máximo)
        WebDriverWait(self.driver, 40).until(ec.presence_of_element_located(self.driver_icon))