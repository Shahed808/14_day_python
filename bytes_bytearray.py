''' 
Name : Mohammad Shahed
Date & Day : Monday 4th July 2022 
Topics : bytes, bytearray, binary forms, escape sequences
Notes : 
          bytes is immutable - modifications cannot be done'''

# r = b'universe'
# print(list(r))                                      # [117, 110, 105, 118, 101, 114, 115, 101]
# print(tuple(r))                                     # (117, 110, 105, 118, 101, 114, 115, 101)
# print(set(r))                                       # {118, 101,117, 110, 105,114, 115, 101}
# print(dict(r))                                      # TypeError: cannot convert dictionary update sequence element #0 to a sequence

# print(r[0])                                         #  117                      
# print(r[-1])                                        # 101
# print(ord('u'))

# r[1] = 118
# print(r)                                               # TypeError: 'bytes' object does not support item assignment


''' bytearray toppic
   bytearray is mutable datatype - modifications can be done'''

# t = bytearray('programming')
# print(t,type(t))                                       # TypeError: string argument without an encoding


t = bytearray(b'programming')
# print(t,type(t))                                        # bytearray(b'programming') <class 'bytearray'>
# for i in t:
#     print(i,end=' ')                                    # 112 114 111 103 114 97 109 109 105 110 103 
# print(list(t))                                          # [112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103]
# print(tuple(t))                                         # (112, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103)
# print(set(t))                                           # {97, 103, 105, 109, 110, 111, 112, 114}


t[0]= 100
print(t)                                                # bytearray(b'drogramming')

print(t[0])


x = (b'[1,2,3,4]')
print(list(x))                                           # [91, 49, 44, 50, 44, 51, 44, 52, 93]