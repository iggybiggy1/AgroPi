from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.testcases import LiveServerTestCase
from api.models import Plant, DataPoint
from django.test import TestCase
from selenium import webdriver
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
import time
from pyotp import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLoginFormTest(StaticLiveServerTestCase):
    
    def testLogin(self):
        driver = webdriver.Chrome()
        driver.get('https://agropiproject.herokuapp.com/web/login/')

        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')
        submit_button = driver.find_element_by_id('loginUser')
        time.sleep(2)

        user_name.send_keys('agroPi')
        user_password.send_keys('agroPi123')
        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)

        logout_button = driver.find_element_by_name('logout').click()
    
    def testRegisterGoBack(self):
        driver = webdriver.Chrome()
        driver.get('https://agropiproject.herokuapp.com/web/login/')
        register_button = driver.find_element_by_name('RegisterButton').click()
        time.sleep(2)

        Goback_button = driver.find_element_by_id('back-btn').click()
        time.sleep(2)
    
    def testMove(self):
        driver = webdriver.Chrome()
        driver.get('https://agropiproject.herokuapp.com/web/login/')
        About_button = driver.find_element_by_name('About').click()
        time.sleep(2)
        Contact_button = driver.find_element_by_name('Contact').click()
        time.sleep(2)
        Home_button = driver.find_element_by_name('Home').click()
        time.sleep(2)
    
    def testGoogleAuth(self):
        driver = webdriver.Chrome()
        driver.get('https://agropiproject.herokuapp.com/web/login/')
        googleAuth_button = driver.find_element_by_id('google-login-btn').click()
        time.sleep(2)

        username_input = driver.find_element_by_xpath('//*[@name="identifier"]')
        time.sleep(2)
        submit_button = driver.find_element_by_class_name('VfPpkd-vQzf8d')
        username_input.send_keys('agropiauthenticationsystem@gmail.com')
        submit_button.click()
        time.sleep(1)

    def testRegister(self):
        driver = webdriver.Chrome()
        driver.get('https://agropiproject.herokuapp.com/web/login/')
        register_button = driver.find_element_by_name('RegisterButton').click()

        time.sleep(3)

        user_name = driver.find_element_by_id('username')
        user_name.send_keys('selenium_test')
        user_email = driver.find_element_by_id('email')
        user_email.send_keys('selenium_text@gmail.com')
        user_password1 = driver.find_element_by_id('password')
        user_password1.send_keys('random123!')
        user_password2 = driver.find_element_by_id('confirm-password')
        user_password2.send_keys('random123!')
        time.sleep(3)

        button_register = driver.find_element_by_id('register-btn')
        button_register.send_keys(Keys.RETURN)
        time.sleep(3)

    def testDashboardFeatures(self):
        driver = webdriver.Chrome()
        driver.get('https://agropiproject.herokuapp.com/web/login/')

        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')
        submit_button = driver.find_element_by_name('loginButton')
        time.sleep(2)

        user_name.send_keys('agroPi')
        user_password.send_keys('agroPi123')
        submit_button.send_keys(Keys.RETURN)
        time.sleep(2)

        graphAdd_button = driver.find_element_by_id('add-graph-btn')
        graphAdd_button.click()
        time.sleep(1)
        graphAdd_button.click()
        time.sleep(1)
        graphAdd_button.click()
        time.sleep(2)

        toAdmin_button = driver.find_element_by_name('to_admin')
        toAdmin_button.click()
        time.sleep(2)

        isStaff_button = driver.find_element_by_id('toggle_is_staff').click()
        time.sleep(2)

        profile_button = driver.find_element_by_id('Profile').click()
        time.sleep(2)

        AddPlant_button = driver.find_element_by_id('addPlant').click()
        time.sleep(2)
    
        plant_name = driver.find_element_by_name('name')
        plant_species = driver.find_element_by_name('species')
        plant_best_light = driver.find_element_by_name('best_light')
        plant_light_margin = driver.find_element_by_name('light_margin')
        plant_best_air_humidity = driver.find_element_by_name('best_air_humidity')
        plant_air_humidity_margin = driver.find_element_by_name('air_humidity_margin')
        plant_best_soil_moisture = driver.find_element_by_name('best_soil_moisture')
        plant_soil_moisture_margin = driver.find_element_by_name('soil_moisture_margin')
        plant_best_temperature = driver.find_element_by_name('best_temperature')
        plant_temperature_margin = driver.find_element_by_name('temperature_margin')

        plant_name.send_keys('Selenium')
        plant_species.send_keys('d')
        plant_best_light.send_keys('10')
        plant_light_margin.send_keys('20')
        plant_best_air_humidity.send_keys('15')
        plant_air_humidity_margin.send_keys('45')
        plant_best_soil_moisture.send_keys('30')
        plant_soil_moisture_margin.send_keys('70')
        plant_best_temperature.send_keys('5')
        plant_temperature_margin.send_keys('25')
        time.sleep(3)

        plant_addPlant = driver.find_element_by_id('add-plant-btn')
        plant_addPlant.send_keys(Keys.RETURN)
        time.sleep(3)

        plant_button = driver.find_element_by_id('addPlant').click()
        time.sleep(2)

        plant_Cancel = driver.find_element_by_name('Cancel').click()
        time.sleep(2)

        dashboard_button = driver.find_element_by_name('Dashboardplant')
        dashboard_button.click()
        time.sleep(2)

        lgout_button = driver.find_element_by_name('logout')
        lgout_button.click()
        time.sleep(2)