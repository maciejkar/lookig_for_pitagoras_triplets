import math
def pit(s):
    """Function check if exist and give sizes of right triangle which have sum of side equal s
    @pam s: (int) sum of lenght of sides
    @return: (bool, int, int, int, int) (True ,a ,b ,c ,k) if tringle exist otherwise (False ,-1 ,-1 ,-1 ,k) where a, b and c are lenght of this trigle and k is nessesary steps"""
    steps = 0 
    for a in range(1,s):
        for b in range(1,s):
            for c in range(1,s):
                steps += 8
                if a**2 + b**2 == c**2 and a + b + c == s:
                    return True, a, b, c, steps
    
    return False , -1, -1, -1, steps

def pit2(s):
    """Function check if exist and give sizes of right triangle which have sum of side equal s
    @pam s: (int) sum of lenght of sides
    @return: (bool, int, int, int, int) (True ,a ,b ,c ,k) if tringle exist otherwise (False ,-1 ,-1 ,-1 ,k) where a, b and c are lenght of this trigle and k is nessesary steps
    """
    steps = 0 
    for a in range(1,s):
        for b in range(1,s):
            c = s - a -b
            steps += 7
            if a**2 + b**2 == c**2:
                return True, a, b, c, steps
    
    return False , -1, -1, -1, steps


def pit3(s):
    """Function check if exist and give sizes of right triangle which have sum of side equal s
    @pam s: (int) sum of lenght of sides
    @return: (bool, int, int, int, int) (True ,a ,b ,c ,k) if tringle exist otherwise (False ,-1 ,-1 ,-1 ,k) where a, b and c are lenght of this trigle and k is nessesary steps
    """
    steps = 0 
    for a in range(1,s):
        for b in range(1,s - a):
            c = s - a -b
            steps += 7
            if a**2 + b**2 == c**2:
                return True, a, b, c, steps
    
    return False , -1, -1, -1, steps

def pit4(s):
    """Function check if exist and give sizes of right triangle which have sum of side equal s
    @pam s: (int) sum of lenght of sides
    @return: (bool, int, int, int, int) (True ,a ,b ,c ,k) if tringle exist otherwise (False ,-1 ,-1 ,-1 ,k) where a, b and c are lenght of this trigle and k is nessesary steps
    """
    steps = 0 
    for a in range(1,s // 2): # a + b > c
        for b in range(1,s - a):
            c = s - a -b
            steps += 7
            if a**2 + b**2 == c**2:
                return True, a, b, c, steps
    
    return False , -1, -1, -1, steps

def pit5(s):
    """Function check if exist and give sizes of right triangle which have sum of side equal s
    @pam s: (int) sum of lenght of sides
    @return: (bool, int, int, int, int) (True ,a ,b ,c ,k) if tringle exist otherwise (False ,-1 ,-1 ,-1 ,k) where a, b and c are lenght of this trigle and k is nessesary steps
    """
    steps = 0 
    for a in range(1,s // 2): 
        for b in range((s- 2*a)//2 ,s - a): # a + b > c => b > (s-2a)/2
            c = s - a -b
            steps += 7
            if a**2 + b**2 == c**2:
                return True, a, b, c, steps
    
    return False , -1, -1, -1, steps

def pit6(s):
    """Function check if exist and give sizes of right triangle which have sum of side equal s
    @pam s: (int) sum of lenght of sides
    @return: (bool, int, int, int, int) (True ,a ,b ,c ,k) if tringle exist otherwise (False ,-1 ,-1 ,-1 ,k) where a, b and c are lenght of this trigle and k is nessesary steps
    """
    steps = 0 
    for a in range(1,s // 2): 
        for b in range((s- 2*a)//2 ,s - 2*a): # a < c
            c = s - a -b
            steps += 7
            if a**2 + b**2 == c**2:
                return True, a, b, c, steps
    
    return False , -1, -1, -1, steps

def pit7(s):
    """Function check if exist and give sizes of right triangle which have sum of side equal s
    @pam s: (int) sum of lenght of sides
    @return: (bool, int, int, int, int) (True ,a ,b ,c ,k) if tringle exist otherwise (False ,-1 ,-1 ,-1 ,k) where a, b and c are lenght of this trigle and k is nessesary steps
    """
    steps = 0 
    for a in range(1,s // 3): # b <c
        for b in range((s- 2*a)//2 ,s - 2*a): 
            c = s - a -b
            steps += 7
            if a**2 + b**2 == c**2:
                return True, a, b, c, steps
    
    return False , -1, -1, -1, steps





if __name__=="__main__":
    # print(pit(1000))
    # print(pit(31))       
    print(pit2(1000))
    print(pit2(31)) 
    print(pit3(1000))
    print(pit3(31)) 
    print(pit4(1000))
    print(pit4(31)) 
    print(pit5(1000))
    print(pit5(31)) 
    print(pit6(1000))
    print(pit6(31)) 
    print(pit7(1000))
    print(pit7(31)) 


