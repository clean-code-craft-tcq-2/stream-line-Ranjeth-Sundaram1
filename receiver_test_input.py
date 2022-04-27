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

update_extremes_expt_outcome_test1 = {'minimum_value': 10, 'maximum_value': 25, 'moving_avg': 0, 'moving_window': [0,0,0,0,0], 'index_of_next_item': -5}
update_extremes_expt_outcome_test2 = {'minimum_value': 0, 'maximum_value': 5, 'moving_avg': 0, 'moving_window': [0,0,0,0,0], 'index_of_next_item': -5}

update_moving_average_expt_outcome_test1 = {'minimum_value': 10, 'maximum_value': 5, 'moving_avg': 0, 'moving_window': [2, 0, 0, 0, 0], 'index_of_next_item': -4}
update_moving_average_expt_outcome_test2 = {'minimum_value': 10, 'maximum_value': 5, 'moving_avg': 1.0, 'moving_window': [0, 0, 0, 5, 0], 'index_of_next_item': 4}

setup_expt_outcome_test1 = [{'minimum_value': None, 'maximum_value': None, 'moving_avg': None, 'moving_window': [None, None, None, None, None], 'index_of_next_item': -5}, {'minimum_value': None, 'maximum_value': None, 'moving_avg': None, 'moving_window': [None, None, None, None, None], 'index_of_next_item': -5}]
