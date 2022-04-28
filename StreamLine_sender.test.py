import unittest
import StreamLine_sender

class TypewiseTest(unittest.TestCase):
    def test_PrintSenderReadings(self):
        self.assertTrue(StreamLine_sender.PrintSenderReadingsInConsole([{"current": 22, "temp": 30}, {"current": 21, "temp": 29}]) == "{'current': 22, 'temp': 30},\n{'current': 21, 'temp': 29}")
        self.assertTrue(StreamLine_sender.PrintSenderReadingsInConsole([{"current": 22, "temp": 30}]) == "{'current': 22, 'temp': 30}")
        self.assertTrue(StreamLine_sender.PrintSenderReadingsInConsole([]) == '')

    def test_IgnoreInvalidSamples(self):
        self.assertTrue(StreamLine_sender.IgnoreInvalidSamples([1122, 2555, 3214, 4094]) == [1122, 2555, 3214, 4094])
        self.assertTrue(StreamLine_sender.IgnoreInvalidSamples([4503, 4094]) == [4094])
        self.assertTrue(StreamLine_sender.IgnoreInvalidSamples([4503]) == [])
        self.assertTrue(StreamLine_sender.IgnoreInvalidSamples([]) == [])
    
    def test_PreProcessSamplesFromA2D_12B(self):
        self.assertTrue(StreamLine_sender.PreProcessSamplesFromA2D_12B([1122, 1800, 3521, 2555, 2022, 3214, 4094], 30) == [8, 13, 26, 19, 15, 24, 30])
        self.assertTrue(StreamLine_sender.PreProcessSamplesFromA2D_12B([1122, 4095, 3214 ], 40) == [11, 31])
        self.assertTrue(StreamLine_sender.PreProcessSamplesFromA2D_12B([], 30) == [])

    def test_GenerateSamples(self):
        self.assertTrue(len(StreamLine_sender.GenerateSamples(10, 10))==10)
        self.assertTrue(max(StreamLine_sender.GenerateSamples(10, 10))<=10)  

    def test_GenerateSamplesToReceiverFromA2D_12B(self):
        self.assertTrue(len(StreamLine_sender.GenerateSamplesToReceiverFromA2D_12B(10)) == 10)

unittest.main(),
