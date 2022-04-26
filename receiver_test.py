import receiver
import unittest
import receiver_test_input

class receiver_test(unittest.TestCase):
    def test_update_extremes(self):
        self.assertTrue(receiver.update_extremes(receiver_test_input.meta_data_sample1.copy(), 25) == receiver_test_input.update_extremes_expt_outcome_test1)
        self.assertTrue(receiver.update_extremes(receiver_test_input.meta_data_sample1.copy(), 0) == receiver_test_input.update_extremes_expt_outcome_test2)
    
    def test_update_moving_average(self):
        self.assertTrue(receiver.update_moving_average(receiver_test_input.meta_data_sample1.copy(), 2) == receiver_test_input.update_moving_average_expt_outcome_test1)
        self.assertTrue(receiver.update_moving_average(receiver_test_input.meta_data_sample2.copy(), 5) == receiver_test_input.update_moving_average_expt_outcome_test2)
        
    def test_setup(self):
        self.assertTrue(str(receiver.setup(5)) == str(receiver_test_input.setup_expt_outcome_test1))
# test

#     def test_pick_sample_from_console(self):
#         self.assertTrue(receiver.pick_sample_from_console([]) == "")
#         self.assertTrue(receiver.pick_sample_from_console(["{'Current': 8, 'Temp': 39}"]) == "Current\t: Min = 8\tMax = 8\tAvg = None\nTemp\t: Min = 39\tMax = 39\tAvg = None\n")

unittest.main(),
