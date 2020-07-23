import unittest
import time
from Api_autotest_v3.Common import HTMLTestRunner
from Api_autotest_v3.Test_case.test_case_user import TestSign


if __name__ == '__main__':
    # select test case in Test_case folder
    cases = unittest.TestLoader().loadTestsFromTestCase(TestSign)

    suite = unittest.TestSuite([cases])

    # run HTMLTestRunner and create a report
    now = time.strftime("%Y-%m-%d")
    filename = 'SCM_lite_' + now + '_api_test_report.html'
    with(open('./Test_report/' + filename, 'wb')) as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='The SCM_Lite API test report',
            description='Run the SCM_Lite Basic flow testing'
        )
        runner.run(suite)
