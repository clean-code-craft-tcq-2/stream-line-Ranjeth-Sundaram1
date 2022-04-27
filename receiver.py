import ast
import enum

data = ""

class Parameter(enum.IntEnum):
    Current = 0
    Temp = 1
    Parameter_Count = 2
            
parameter_wise_metadata = []

moving_window_size = None
whitelisted_metadata = {"minimum_value" : "Min" ,"maximum_value" : "Max","moving_avg" : "Avg"}

def setup(l_moving_window_size):
    global moving_window_size 
    moving_window_size = l_moving_window_size
    
    meta_data_sample = {
                        "minimum_value"     : None,
                        "maximum_value"     : None ,
                        "moving_avg"        : None,
                        "moving_window"     : None,
                        "index_of_next_item": -moving_window_size,
                        }
    for param in range (Parameter.Parameter_Count ):
        parameter_wise_metadata.append(meta_data_sample.copy())
        parameter_wise_metadata[param]["moving_window"] = [None] * moving_window_size
    return parameter_wise_metadata

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
    output_to_console()


def output_to_console():
    data_to_print = ""
    for param in range (Parameter.Parameter_Count ):
        data_to_print += f"{Parameter(param).name}\t: "
        for data in whitelisted_metadata:
            data_to_print += f"{whitelisted_metadata[data]} = {parameter_wise_metadata[param][data]}\t"    
        data_to_print += "\n"
    print (data_to_print)
    

# setup(5)
# pick_sample_from_console(data) 


