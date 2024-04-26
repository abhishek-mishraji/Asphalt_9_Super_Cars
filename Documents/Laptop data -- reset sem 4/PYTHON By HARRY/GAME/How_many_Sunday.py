s = 0

f_year = 2021
f_m = 1
f_d = 1
# ?***********?
l_year = 2022
l_m = 12
l_d = 30
# *********
c_year = 2021
c_m = 12
c_d = 30
# **************
if(f_year <= c_year):
    while(c_year >= f_year):
        c_year = c_year-1
        # **********
        while(c_m >= f_m):
            c_m = c_m-1
            if(s >= 1):
                c_d = c_d+30
            # ***************
            while(c_d >= f_d):

                c_d = c_d-7
                s = s+1
                # **********************************
                # **************************
# if(l_year > c_year):
#     while(c_year <= l_year):
#         c_year = c_year+1
#         # **********
#         while(c_m <= l_m):
#             c_m = c_m+1
#             if(s >= 1):
#                 c_d = c_d+30
#             # ***************
#             while(c_d <= l_d):

#                 c_d = c_d-7
#                 s = s+1
print(s)
