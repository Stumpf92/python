def bittodec(list_8):
    sum=0
    for i in range(8):
        sum = sum + list_8[i]*2**(7-i)
    
    return str(sum)




def int32_to_ip(int32):
    bit32_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(32):
        if 2**(32-i-1) <= int32:
            bit32_list[i] = 1
            int32 = int32 - 2**(32-i-1)
    
    print(bit32_list)

    quarter = [0,0,0,0]
    quarter[0] = bit32_list[:8]
    quarter[1] = bit32_list[8:16]
    quarter[2] = bit32_list[16:24]
    quarter[3] = bit32_list[24:]
    print(quarter)

    end = bittodec(quarter[0])+"."+bittodec(quarter[1])+"."+bittodec(quarter[2])+"."+bittodec(quarter[3])
    print(end)
    return(end)    
    
 


int32_to_ip(1024)