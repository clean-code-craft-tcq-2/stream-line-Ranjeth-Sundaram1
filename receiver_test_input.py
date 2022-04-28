# metadata
meta_data_sample1 = {
                    "minimum_value"     : 10,
                    "maximum_value"     : 5 ,
                    "moving_avg"        : 0,
                    "moving_window"     : [0,0,0,0,0],
                    "index_of_next_item": -5,
                    }

meta_data_sample2 = {
                    "minimum_value"     : 10,
                    "maximum_value"     : 5 ,
                    "moving_avg"        : 0,
                    "moving_window"     : [0,0,0,0,0],
                    "index_of_next_item": 3,
                    }
received_data1 = "{'Current': 8, 'Temp': 39}"
received_data2 = ["{'Current': 8, 'Temp': 39}","{'Current': 8, 'Temp': 39}","{'Current': 8, 'Temp': 39}","{'Current': 8, 'Temp': 39}","{'Current': 8, 'Temp': 39}"]


update_extremes_expt_outcome_test1 = {'minimum_value': 10, 'maximum_value': 25, 'moving_avg': 0, 'moving_window': [0,0,0,0,0], 'index_of_next_item': -5}
update_extremes_expt_outcome_test2 = {'minimum_value': 0, 'maximum_value': 5, 'moving_avg': 0, 'moving_window': [0,0,0,0,0], 'index_of_next_item': -5}

update_moving_average_expt_outcome_test1 = {'minimum_value': 10, 'maximum_value': 5, 'moving_avg': 0, 'moving_window': [2, 0, 0, 0, 0], 'index_of_next_item': -4}
update_moving_average_expt_outcome_test2 = {'minimum_value': 10, 'maximum_value': 5, 'moving_avg': 1.0, 'moving_window': [0, 0, 0, 5, 0], 'index_of_next_item': 4}

setup_expt_outcome_test1 = [{'minimum_value': None, 'maximum_value': None, 'moving_avg': None, 'moving_window': [None, None, None, None, None], 'index_of_next_item': -5}, {'minimum_value': None, 'maximum_value': None, 'moving_avg': None, 'moving_window': [None, None, None, None, None], 'index_of_next_item': -5}]

output_test1 = [{'minimum_value': 8, 'maximum_value': 8, 'moving_avg': None, 'moving_window': [8, None, None, None, None], 'index_of_next_item': -4}, {'minimum_value': 39, 'maximum_value': 39, 'moving_avg': None, 'moving_window': [39, None, None, None, None], 'index_of_next_item': -4}]
output_test2 = [{'minimum_value': 8, 'maximum_value': 8, 'moving_avg': 8.0, 'moving_window': [8, 8, 8, 8, 8], 'index_of_next_item': 0}, {'minimum_value': 39, 'maximum_value': 39, 'moving_avg': 39.0, 'moving_window': [39, 39, 39, 39, 39], 'index_of_next_item': 0}]
