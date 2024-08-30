import pytest
import softest
import time
from pages.yatra_launch_page import LaunchPage
from selenium.webdriver.common.by import By
from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResults
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    
    def test_search_flights(self):
        lp = LaunchPage(self.driver)
        
        time.sleep(2)
        #Provide going from Location
        lp.enterDepartFromLocation("New Delhi")
        time.sleep(2)
        
        #Provide going to Location
        lp.enterGoingToLocation("New York")
        time.sleep(2)
        
        #Selecting the date
        lp.enterDepartureDate("12/09/2024")
        time.sleep(2)
        
        #Clicking on Flight Search button
        lp.clickSearchButton()
        time.sleep(2)
        
        #Handling the dynamic scroll
        lp.page_scroll()
        time.sleep(2)
        
        #Select filter for 1 Stop
        sf = SearchFlightResults(self.driver)
        sf.filter_flights()
   
        allStops = lp.wait_for_presence_of_elements(By.XPATH, "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")
        print(allStops)
        
        ut = Utils()
        ut.assertListItemText(allStops, "1 Stop")
        

