import receiver
import unittest
import receiver_test_input

class receiver_test(unittest.TestCase):
    def test_update_extremes(self):
        self.assertTrue(receiver.update_extremes(receiver_test_input.meta_data_sample1, 25) == {'minimum_value': 10, 'maximum_value': 25, 'moving_avg': 0, 'moving_window': 5, 'index_of_next_item': -5})
        self.assertTrue(receiver.update_extremes(receiver_test_input.meta_data_sample1, 0) == {'minimum_value': 0, 'maximum_value': 5, 'moving_avg': 0, 'moving_window': 5, 'index_of_next_item': -5})
    
    def test_pick_sample_from_console(self):
        self.assertTrue(receiver.pick_sample_from_console([]) == "")

unittest.main(),
