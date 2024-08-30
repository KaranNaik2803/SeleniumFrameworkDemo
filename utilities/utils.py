import softest 

class Utils(softest.TestCase):
    def assertListItemText(self, aList, value):
        for stop in aList:
            print("********The Text is: " + stop.text + "********")
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("*******Test Passed*******")
            else:
                print("!!!!!Test has Failed!!!!!")
        self.assert_all()