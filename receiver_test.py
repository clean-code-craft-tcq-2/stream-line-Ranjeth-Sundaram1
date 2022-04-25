import receiver
import unittest
import receiver_test_input

class receiver_test(unittest.TestCase):
  
  def test(self):
    self.assertTrue((receiver.update_extremes(receiver_test_input.meta_data_sample1, 25) == {'minimum_value': 10, 'maximum_value': 25, 'moving_avg': 0, 'moving_window': 5, 'index_of_next_item': -5})
        
unittest.main(),
