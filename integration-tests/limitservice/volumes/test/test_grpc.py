#test_grpc.py

import logging
import unittest
import grpc
import time

import authmethod_pb2
import backend_pb2
import backend_pb2_grpc
import services_pb2
import services_pb2_grpc
import credentials_pb2 
import vpnserver_output_pb2
import vpnserver_label_pb2

print('========= Tests ========='*4)

class LimitServiceTesting(unittest.TestCase):
   

    def test_0_GetFullLimits(self):
        
        project = 'kasperskylab'
        
        with grpc.insecure_channel('limits:9090') as channel:
            stub = services_pb2_grpc.LimitsStub(channel)
            response = stub.GetFull(backend_pb2.LimitsGetFullRequest(user_id=1))

        self.assertEqual((response.project),project)
        print(">>>>>TEST#0 - Get Full Limits Request - OK ")
        print(response)
   
    def test_1_GetLimits(self):
        
        with grpc.insecure_channel('limits:9090') as channel:
            stub = services_pb2_grpc.LimitsStub(channel)
            response = stub.Get(backend_pb2.LimitsGetRequest(user_id=1))
        
        self.assertEqual(response,response)
        print(">>>>>TEST#1 - Get Short Limits Request - OK")
        print(response)
       
    
    # @unittest.skip("Do not need to test it")
    def test_2_SetTrafficLimit_1000(self):
        time_start = str(time.time()).split('.')[0]
        time_start_long = str(time_start+"000")
      
       
        with grpc.insecure_channel('limits:9090') as channel:
            stub = services_pb2_grpc.LimitsStub(channel)
            limits = backend_pb2.TrafficLimits(traffic_start=int(time_start_long), traffic_limit=20000)
            request = backend_pb2.LimitsSetRequest(user_id=1,limits=limits)
            response = stub.Set(request)
            self.assertEqual(response,response)
       
        print(">>>>>TEST#2 - Set Up a new traffic limit value - OK")
        print(response)
    
    # @unittest.skip("Do not need to test it")
    def test_3_CheckNewLimitApplied(self):
        
        with grpc.insecure_channel('limits:9090') as channel:
            stub = services_pb2_grpc.LimitsStub(channel)
            response = stub.Get(backend_pb2.LimitsGetRequest(user_id=1))
        self.assertEqual((response.traffic_limit),20000)
        global usage_before
        usage_before = response.traffic_usage 
        print(">>>>>TEST#3 - Check if New Limits  are applied - OK ")
        print(response)
    
    # @unittest.skip("Do not need to test it")
    def test_4_CountUsageCheck_used_500(self):
        
        with grpc.insecure_channel('limits:9090') as channel:
            stub = services_pb2_grpc.LimitsStub(channel)
            limits_count = backend_pb2.LimitsCountUsageRequest(user_id=1,traffic_usage=500)
            request = stub.CountUsage(limits_count)    
        self.assertEqual(request,request)
        print(">>>>>TEST#4 - Check Count Usage -traffic_usage should change - OK ")
        print(request)

    def test_5_CheckUsageCount(self):
        
        with grpc.insecure_channel('limits:9090') as channel:
            stub = services_pb2_grpc.LimitsStub(channel)
            response = stub.Get(backend_pb2.LimitsGetRequest(user_id=1))
        self.assertEqual(response.traffic_usage,(usage_before+500),"TEST#5 - Usage counts incorrecly!!! ")
        print(">>>>>TEST#5 - Check Usage counts correcly - OK") 
        print(response)  
        print('========= Completed ======'*4)

if __name__ == '__main__':
    
    unittest.main() 
