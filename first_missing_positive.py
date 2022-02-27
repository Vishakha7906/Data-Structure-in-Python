 ​class  ​Solution :
 ​    ​def​ ​firstMissingPositive​(​self​, ​nums​) :
 ​        ​     ​n​ ​=​ ​len(​nums​) 
 ​       ​for ​i​ ​in range​(​n​): 
 ​            ​# To determine whether this number can be exchanged.
 ​            while nums​[i]>0​ ​and ​nums​[​i​]​<=​n​ ​and ​nums​[​i​]​!=​nums​[​nums​[​i​]​-​1​] : 
 ​                ​self​.​swap​(​nums​,​i​,​nums​[​i​]​-​1​) 
 ​        ​for ​i​ ​in ​range​(​n​) : 
 ​            ​if ​nums​[​i​]​ !=​i​+​1​: 
 ​                ​return ​i​+​1 
 ​        ​return ​n​+​1 
 ​    ​def swap(​self​,​ nums​, i,​ j​) : 
 ​        ​nums​[​i​] ,​ nums​[​j​] ​=​ ​nums​[​j​] ,​ nums​[​i​]