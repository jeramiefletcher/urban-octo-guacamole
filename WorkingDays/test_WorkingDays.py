import unittest
from WorkingDays import *
import WorkingDays
from tests.testSetup import *

__version__ = '0.20200523'
printVersion(__version__, WorkingDays.__name__, WorkingDays.__version__)


class DateCleanupTests(unittest.TestCase):
    def test_epochFormat(self):
        self.assertEqual(dateCleanup(1571824800000,
                                     epoch=True).strftime("%Y%m%d%H%M%S"),
                         '20191023100000')

    def test_TZFormat(self):
        self.assertEqual(dateCleanup('2015-03-26T10:58:51Z'
                                     ).strftime("%Y%m%d%H%M%S"),
                         '20150326105851')

    def test_germanDateFormat(self):
        self.assertEqual(dateCleanup('07.04.2020').strftime("%Y%m%d%H%M%S"),
                         '20200407000000')

    def test_germanDateFormatWithTime(self):
        self.assertEqual(dateCleanup
                         ('07.04.2020 12:12:12').strftime("%Y%m%d%H%M%S"),
                         '20200407121212')

    def test_alphaDateFormat(self):
        self.assertEqual(dateCleanup
                         ('march 25, 2020').strftime("%Y%m%d%H%M%S"),
                         '20200325000000')

    def test_alphaDateShortFormat(self):
        self.assertEqual(dateCleanup
                         ('MAR 25 2020').strftime("%Y%m%d%H%M%S"),
                         '20200325000000')

    def test_DateWithTimeFormat(self):
        self.assertEqual(dateCleanup
                         ('2020-02-28 12:30:00').strftime("%Y%m%d%H%M%S"),
                         '20200228123000')

    def test_DateWithTimeNoSeperationFormat(self):
        self.assertEqual(dateCleanup
                         ('2020-02-2812:30:00').strftime("%Y%m%d%H%M%S"),
                         '20200228123000')

    def test_DateWithColonTimeNoSeperationFormat(self):
        self.assertEqual(dateCleanup
                         ('2020:02:2812:30:00').strftime("%Y%m%d%H%M%S"),
                         '20200228123000')

    def test_DayLessThanTweleve(self):
        self.assertEqual(dateCleanup
                         ('2020-02-05').strftime("%Y%m%d%H%M%S"),
                         '20200205000000')

    def test_DateString(self):
        self.assertEqual(dateCleanup
                         ('20200205000000').strftime("%Y%m%d%H%M%S"),
                         '20200205000000')


class WorkdayTests(unittest.TestCase):

    def test_WeekendBetweenOffset(self):
        self.assertEqual(workday('08.04.2020', 3), '20200413')

    def test_NoWeekendBetweenOffset(self):
        self.assertEqual(workday('20200408', 2), '20200410')

    def test_FridayStart(self):
        self.assertEqual(workday('10.04.2020', 3), '20200415')

    def test_SaturdayStart(self):
        self.assertEqual(workday('11.04.2020', 3), '20200415')

    def test_SundayStart(self):
        self.assertEqual(workday('11.04.2020', 3), '20200415')


class CompareWorkingdaysTests(unittest.TestCase):

    def test_WeekendBetweenOffset(self):
        self.assertEqual(compareWorkingdays('08.04.2020', '20200413'), 3)

    def test_NoWeekendBetweenOffset(self):
        self.assertEqual(compareWorkingdays('20200408', '20200410'), 2)


class CompareLastWorkdayofMonthTests(unittest.TestCase):

    def test_Feb(self):
        self.assertEqual(lastWorkdayofMonth('20200213'), '20200228')

    def test_LastDayNotWeekend(self):
        self.assertEqual(lastWorkdayofMonth('20200413'), '20200430')

    def test_LastDayWeekend(self):
        self.assertEqual(lastWorkdayofMonth('20200513'), '20200529')


class CompareLastWorkdayofQtrTests(unittest.TestCase):
    quarters = {"Q1": ["Nov", "Dec", "Jan"],
                "Q2": ["Feb", "Mar", "Apr"],
                "Q3": ["May", "Jun", "Jul"],
                "Q4": ["Aug", "Sep", "Oct"]}

    def test_CalendarQtr(self):
        self.assertEqual(lastWorkdayofQtr('20200213'), '20200331')

    def test_FiscalQtr(self):
        self.assertEqual(lastWorkdayofQtr('20200213', key=self.quarters),
                         '20200430')

    def test_FiscalQtrList(self):
        self.assertEqual(lastWorkdayofQtr('20200213',
                                          Q1=["Nov", "Dec", "Jan"],
                                          Q2=["Feb", "Mar", "Apr"]),
                         '20200430')

    def test_FiscalQtrEndsonWeekend(self):
        self.assertEqual(lastWorkdayofQtr('20200913', key=self.quarters),
                         '20201030')


class CompareLastDayofMonthTests(unittest.TestCase):

    def test_Feb(self):
        self.assertEqual(lastDayofMonth('20200213'), '20200229')

    def test_LastDay31(self):
        self.assertEqual(lastDayofMonth('20200313'), '20200331')

    def test_LastDay30(self):
        self.assertEqual(lastDayofMonth('20200413'), '20200430')


"""
if __name__ == '__main__':
    unittest.main()
"""
suites = []
tests = [DateCleanupTests,
         WorkdayTests,
         CompareWorkingdaysTests,
         CompareLastWorkdayofMonthTests,
         CompareLastWorkdayofQtrTests,
         CompareLastDayofMonthTests]
for test_class in tests:
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    suites.append(suite)
big_suite = unittest.TestSuite(suites)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(big_suite)
