from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):  

	def setUp(self):  
		self.browser = webdriver.Firefox()

	def tearDown(self):  
		self.browser.quit()

	def test_can_gender_a_text(self):  
		# Edith has heard about a cool new online texte gendern app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention texte gendern
		self.assertIn('Texte automatisch gendern', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Texte automatisch gendern', header_text)

		# She is invited to enter a text straight away
		inputbox = self.browser.find_element_by_id('id_new_text')
		self.assertEqual(inputbox.get_attribute('placeholder'),
		'Text hier einfügen.')
		# She types "Die Studenten sind jetzt eingeschrieben. Sie werden Weggefährten und vielleicht auch Freunde."
		# into a text box (Edith is eine kitschige Erstsemesterin)
		inputbox.send_keys('Die Studenten sind jetzt eingeschrieben. Sie werden Weggefährten und vielleicht auch Freunde')

		# When she hits enter, the page updates, and now the page lists
		# "Die Studierenden sind jetzt eingeschrieben. Sie werden ka muss ihc gucken" as an output in a box underneath.
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
	
		textbox = self.browser.find_element_by_id('id_gender_output')
		self.assertTrue(textbox.text == 'Die Studierenden sind jetzt eingeschrieben. Sie werden ka muss ihc gucken')

		# Satisfied, she goes back to sleep

if __name__ == '__main__':  
	unittest.main(warnings='ignore')
