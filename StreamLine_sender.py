import random
import sys

global defaultParams 
defaultParams = {}
defaultParams['max_current'] = 30 # in Amps
defaultParams['max_temp']    = 40 # in Degree celsius
defaultParams['max_bit_value'] = 4094

def PrintSenderReadingsInConsole(DataToPrint: list):
    messageToPrint = ',\n'.join(str(one_set)for one_set in DataToPrint)
    print (type(messageToPrint))
    print(messageToPrint)
    return(messageToPrint)

def IgnoreInvalidSamples(input_samples : list):
    if input_samples != []:
        samples_to_examine = [sample for sample in input_samples if sample in range (0, defaultParams['max_bit_value']+1)]
        return samples_to_examine
    return input_samples

def PreProcessSamplesFromA2D_12B(input_samples: list, max_value:int):
    samples_to_examine = IgnoreInvalidSamples(input_samples)
    samples_to_examine = [round(sample*max_value/defaultParams['max_bit_value']) for sample in samples_to_examine]
    return samples_to_examine

def GenerateSamples(Samples_count: int, max_sample_value: int):
    Samples = []
    for i in range(0, Samples_count):
        sample = random.randint(0,defaultParams['max_bit_value'])
        Samples.append(sample)
    Samples = PreProcessSamplesFromA2D_12B(Samples, max_sample_value) 
#     print (Samples)
    return Samples

def GenerateSamplesToReceiverFromA2D_12B(Samples_count):
    samplesToReceiver =[]
    current_samples = GenerateSamples(Samples_count, defaultParams['max_current'])
    temp_samples = GenerateSamples(Samples_count, defaultParams['max_temp'])
    min_Samples = len(current_samples) if len(current_samples)< len(temp_samples) else len(temp_samples)
    for count in range (0, min_Samples):
        dict_out = {'Current': current_samples[count], 'Temp' : temp_samples[count]}
#         sys.stdout.write(f"{dict_out}\n")
        print (dict_out)
        samplesToReceiver.append(dict_out)
#     print(len(samplesToReceiver))
#     PrintSenderReadingsInConsole(samplesToReceiver)
    return samplesToReceiver

GenerateSamplesToReceiverFromA2D_12B(50)
