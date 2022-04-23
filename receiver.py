import ast
import enum

class Parameter(enum.IntEnum):
    Current = 0
    Temp = 1
    Parameter_Count = 2

data = [
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
"{'Current':10, 'Temp':20}",
]
            
parameter_wise_metadata = []

moving_window_size = 5
def setup():
    meta_data_sample = {
                        "minimum_value"     : None,
                        "maximum_value"     : None ,
                        "moving_avg"        : None,
                        "moving_window"     : None,
                        "index_of_next_item": -5,
                        }
    for param in range (Parameter.Parameter_Count ):
        parameter_wise_metadata.append(meta_data_sample.copy())
        parameter_wise_metadata[param]["moving_window"] = [None] * moving_window_size


def pick_sample_from_console(data_stream):
    for sample in data_stream:        
        dictionary = ast.literal_eval(sample)
        process_sample(dictionary)

        
def update_extremes(meta_data, new_data_point):
    if (meta_data["minimum_value"] == None):
        meta_data["minimum_value"] = new_data_point
        meta_data["maximum_value"] = new_data_point
    else:
        meta_data["minimum_value"] = min(meta_data["minimum_value"],new_data_point)
        meta_data["maximum_value"] = max(meta_data["maximum_value"],new_data_point)
    return meta_data


def update_moving_average(meta_data, new_data_point):
    meta_data["moving_window"][meta_data["index_of_next_item"]] = new_data_point
    if meta_data["index_of_next_item"] < moving_window_size-1:
        meta_data["index_of_next_item"] += 1
    else:
        meta_data["index_of_next_item"] = 0
    if( meta_data["index_of_next_item"] >= 0):
        meta_data["moving_avg"] = sum(meta_data["moving_window"])/moving_window_size
    return meta_data
    
        
def process_sample(sample):
    for param in range (Parameter.Parameter_Count ):
        update_extremes(parameter_wise_metadata[param], sample[(Parameter(param).name)])
        update_moving_average(parameter_wise_metadata[param], sample[(Parameter(param).name)])

def output_to_console():
    print ()
    
setup()
pick_sample_from_console(data)     
print (parameter_wise_metadata[0])   
print (parameter_wise_metadata[1])   



