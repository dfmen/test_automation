from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from assertions import AssertionsTest
from search import SearchTest

#Loading the TCs from the files
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

#Creating a TestSuite with both sets of TCs
smoke_test = TestSuite([assertions_test, search_test])

#Parameters to generate reports, through a dictionary
kwargs = {
    "output": "smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": False
}

#To generate HTML "cool" reports
runner = HTMLTestRunner(**kwargs)

#To run the TestSuite "Where the fun begins!"
runner.run(smoke_test)