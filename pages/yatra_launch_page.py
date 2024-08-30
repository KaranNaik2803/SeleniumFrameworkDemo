import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_driver import BaseDriver

class LaunchPage(BaseDriver):
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver       
    
    #Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id= 'BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"
    
    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)
    
    def enterDepartFromLocation(self, departLocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departLocation)
        self.getDepartFromField().send_keys(Keys.ENTER) 

#Enter Going To Location     
    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)
    
    def getAllSearchResults(self):
        return self.wait_for_presence_of_elements(By.XPATH, self.GOING_TO_RESULT_LIST)
    
    def enterGoingToLocation(self, goingToLocation):
        self.getGoingToField().click()
        time.sleep(2)
        self.getGoingToField().send_keys(goingToLocation)
        search_results = self.getAllSearchResults()
        
        for results in search_results:
            if goingToLocation in results.text:
                results.click()
                break
          
#Select Dates
    def getDepartureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE)
          
    def getAllDateFieldsField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)     
    
    def enterDepartureDate(self, departuredate):
        self.getDepartureDateField().click()
        all_dates = self.getAllDateFieldsField().find_elements(By.XPATH, self.ALL_DATES)
        
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break
#search button
    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)
            
    def clickSearchButton(self):
        self.getSearchButton().click()
        time.sleep(4)