'''
Created on 19 Mar 2010

@author: zak
'''

class Problem28(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def run(self):
        sum = 1
        count = 1
        for i in range(1, 501):
            side = i*2
            for j in range(1,5):
                count = count + side
                sum = sum + count
                
        print(sum)
        
if __name__ == "__main__":
    solver = Problem28()
    solver.run()
            
            
        