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
        result = (receiver.setup(5))
        index = 0
        print (result)
        print (receiver_test_input.setup_expt_outcome_test1)
        for item in result:
            self.assertTrue(item == receiver_test_input.setup_expt_outcome_test1[index])
            index += 1
            
    def test_process_sample(self):
        setup(5)
        process_sample(receiver_test_input.received_data1)
        self.assertTrue(str(get_parameter_wise_metadata()) == str(output_test1))
        
        setup(5)
        for item in receiver_test_input.received_data2:
            process_sample(item)
        print (get_parameter_wise_metadata())
        self.assertTrue(str(get_parameter_wise_metadata()) == str(output_test2))

unittest.main(),
