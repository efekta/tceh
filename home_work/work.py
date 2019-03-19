# my_list = [41, 17453, 85, 24, 578]
# def all_list(my_list):
#     for nums in my_list:
#         if isinstance (nums, (int,float)):
#             my_list.sort()
#     print(my_list)
#     return my_list
# all_list(my_list)
#
# my_list = [41, 17453, 85, 24, 578]
# def all_list(my_list):
#     for nums in my_list:
#         if isinstance (nums, (int,float)):
#             my_list.sort()
#     print(my_list)
#     return my_list
# all_list(my_list)

my_list = [41, 17453, 85, 24, 578]
def all_list(nums):
    for nums in my_list:
        if nums == type(int):
            my_list.sort()
    print(my_list)

all_list(my_list)