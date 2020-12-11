import unittest
import schedule


class TestSchedule(unittest.TestCase):

    def test_get_timestamp_empty(self):
        res = schedule.get_timestamp('')
        self.assertEqual(res, 1893474000)

    def test_get_timestamp(self):
        res = schedule.get_timestamp('2020-12-01::10:30')
        self.assertEqual(res, 1606836600)

    def test_get_reverse_timestamp(self):
        res = schedule.get_reverse_timestamp(1893474000)
        self.assertEqual(res, '2030-01-01::00:00')

    def test_am_i_double_booked_no_overlap(self):
        res = schedule.am_i_double_booked('./csv/test_schedule1.csv')
        expected = []
        self.assertEqual(res, expected)

    def test_am_i_double_booked_adjacent(self):
        res = schedule.am_i_double_booked('./csv/test_schedule2.csv')
        expected = []
        self.assertEqual(res, expected)

    def test_am_i_double_booked_single_overlap1(self):
        res = schedule.am_i_double_booked('./csv/test_schedule3.csv')
        expected = ['2020-12-01::10:30 - 2020-12-01::11:30 | 2020-12-01::10:50 - 2020-12-01::13:30']
        self.assertEqual(res, expected)

    def test_am_i_double_booked_single_overlap2(self):
        res = schedule.am_i_double_booked('./csv/test_schedule7.csv')
        expected = ['2020-12-01::10:30 - 2020-12-02::19:30 | 2020-12-01::10:50 - 2020-12-01::23:50']
        self.assertEqual(res, expected)

    def test_am_i_double_booked_multiple_overlaps1(self):
        res = schedule.am_i_double_booked('./csv/test_schedule4.csv')
        expected = [
            '2020-12-01::10:30 - 2020-12-01::19:30 | 2020-12-01::10:50 - 2020-12-01::13:30',
            '2020-12-01::10:30 - 2020-12-01::19:30 | 2020-12-01::13:50 - 2020-12-01::14:30'
        ]
        self.assertEqual(res, expected)

    def test_am_i_double_booked_multiple_overlaps2(self):
        res = schedule.am_i_double_booked('./csv/test_schedule5.csv')
        expected = [
            '2020-12-01::10:30 - 2020-12-01::19:30 | 2020-12-01::10:50 - 2020-12-01::13:30',
            '2020-12-01::10:30 - 2020-12-01::19:30 | 2020-12-01::13:20 - 2020-12-01::14:30',
            '2020-12-01::10:50 - 2020-12-01::13:30 | 2020-12-01::13:20 - 2020-12-01::14:30'
        ]
        self.assertEqual(res, expected)

    def test_am_i_double_booked_multiple_overlaps3(self):
        res = schedule.am_i_double_booked('./csv/test_schedule6.csv')
        expected = [
            '2020-12-01::10:30 - 2020-12-01::19:30 | 2020-12-01::10:50 - 2030-01-01::00:00'
        ]
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
