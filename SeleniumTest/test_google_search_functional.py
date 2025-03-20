7.	import unittest
8.	from selenium import webdriver
9.	from selenium.webdriver.common.keys import Keys
10.	from selenium.webdriver.common.by import By
11.	import time
12.	
13.	class GoogleSearchTest(unittest.TestCase):
14.	    def setUp(self):
15.	        """Setup the test environment before each test."""
16.	        # Specify the path to chromedriver if it's not in your PATH
17.	        self.driver = webdriver.Chrome()
18.	
19.	    def test_search_in_google(self):
20.	        """Test searching for 'Python' on Google."""
21.	        driver = self.driver
22.	        driver.get("http://www.google.com")
23.	        self.assertIn("Google", driver.title)
24.	        
25.	        # Find the search box, enter 'Python', and submit the form
26.	        search_box = driver.find_element(By.NAME, "q")
27.	        search_box.send_keys("Python")
28.	        search_box.send_keys(Keys.RETURN) # simulates hitting the Enter key
29.	
30.	        # Wait a few seconds to see the results
31.	        time.sleep(10)
32.	        
33.	        # Check if 'python.org' is in the search results
34.	        self.assertIn("python.org", driver.page_source)

