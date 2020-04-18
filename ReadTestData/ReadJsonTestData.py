import json
class GetTestData:

    def loadTestData(self):
        print("Trying to load Test Data")
        global jsonData
        file=open("../TestData/TestData.json")
        jsonData=json.load(file)
        print("Test Data is loaded SucessFully")

    def getData(self,testcaseName,fieldName):

        for testcase in jsonData["TestCase"]:

            if str(testcase['TestCaseName']).strip()==str(testcaseName).strip():
                return testcase[str(fieldName)]
