import math

def hex_to_bin(number):
    s = "{0:08b}".format(int(number, 16))
    if len(s) == 21:
        return '000' + s
    if len(s) == 22:
        return '00' + s
    if len(s) == 23:
        return '0' + s
    return s

def bin_to_hex(number):
    s = hex(int(number, 2))
    s = s[2:]
    return s

def binary_to_decimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def decimal_to_binary(n):  
    s = bin(n).replace("0b", "")
    if len(s) == 1:
        return '000' + s
    if len(s) == 2:
        return '00' + s
    if len(s) == 3:
        return '0' + s
    return s

def ip(text):
    table = [18,10,2,20,12,4,22,14,6,24,16,8,17,9,1,19,11,3,21,13,5,23,15,7]
    strr = ''
    for i in table:
        strr += text[i-1]
    return strr
    
def expansion(text):
    table = [12,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,1]
    strr = ''
    for i in table:
        strr += text[i-1]
    return strr

def pc1(lis):
    pc = [17, 9, 1, 18, 10, 2, 19, 11,3, 23, 15, 7, 22, 14, 6,21, 13, 5, 20, 12, 4]
    strr = ''
    for i in pc:
        strr += lis[i-1]
    return strr

def pc2(lis):
    pc = [17, 11, 1, 5, 3, 15, 6, 18, 10, 19, 12, 4, 8, 16, 9, 20, 13, 2]
    strr = ''
    for i in pc:
        strr += lis[i-1]
    return strr

def leftshift(lis, hm):
    strr = lis[hm:] + lis[:hm]
    return(strr)

def keygen(lis, key):
    key_list = []
    key1 = key[:10]
    key2 = key[10:]
    for i in lis:
        newkey1 = leftshift(key1, i)
        newkey2 = leftshift(key2, i)
        newkey = newkey1 + newkey2
        newkey = pc2(newkey)
        key_list.append(newkey)
        key1 = newkey1
        key2 = newkey2
        #print(newkey, (newkey1), (newkey2))
    return key_list

def xorr(str1, str2):
    strr = ''
    for i, j in zip(str1, str2):
        if i == j:
            strr += '0'
        else:
            strr += '1'
    return strr

def find_s(s, row, col):
    s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
          [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
          [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
          [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

    s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
          [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
          [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
          [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

    s3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
          [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
          [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
          [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

    lis = [s1, s2, s3]
    #print(lis[1][2][3])
    #print(s-1,row,col)
    return lis[s-1][row][col]

def find_row_col(strr, s):
    row_num = int(strr[:1] + strr[5:])
    col_num = int(strr[1:5])
    row_num = binary_to_decimal(row_num)
    col_num = binary_to_decimal(col_num)
    #print(row_num, col_num)
    return find_s(s, row_num, col_num)

def s_boxing(strr):
    s1 = strr[:6]
    s2 = strr[6:12]
    s3 = strr[12:]

    

    s1 = decimal_to_binary(find_row_col(s1, 1))
    s2 = decimal_to_binary(find_row_col(s2, 2))
    s3 = decimal_to_binary(find_row_col(s3, 3))

    #print(s1, s2, s3)
    
    return(s1+s2+s3)

def inverse_ip(text):
    table = [15, 3, 18, 6, 21, 9, 24,12,14,2,17,5,20,8,23,11,13,1,16,4,19,7,22,10]
    strr = ''
    for i in table:
        strr += text[i-1]
    return strr

def permutation(text):
    table = [7,12,1,5,10,2,8,3,9,6,11,4]
    strr = ''
    for i in table:
        strr += text[i-1]
    return strr

def f(right, subkey):
    right = expansion(right)
    value = xorr(right, subkey)
    cypher = s_boxing(value)
    cypher = permutation(cypher)
    return cypher

def rounds(plain, subkey):
    left = plain[:12]
    right = plain[12:]
    temp = f(right, subkey)
    temp = xorr(left, temp)
    return right+temp

def encrypt_des(plain, key):
    plain = hex_to_bin(plain)
    key = hex_to_bin(key)
    
    plain = ip(plain)
    key = pc1(key)
    key_list = keygen([1,1,2,2,2,2], key)
    
    for subkey in key_list:
        plain = rounds(plain, subkey)

    cypher = plain[12:] + plain[:12]
    cypher = inverse_ip(cypher)
    cypher = bin_to_hex(cypher)
    return cypher

def decrypt_des(cypher, key):
    cypher = hex_to_bin(cypher)
    key = hex_to_bin(key)

    cypher = ip(cypher)
    key_list = keygen([1,1,2,2,2,2], key)

    for subkey in reversed(key_list):
        cypher = rounds(cypher, subkey)

    
    
















