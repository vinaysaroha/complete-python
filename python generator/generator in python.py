# output complete memory occupy na kare uske liye hota hai yield function , ye function he generator kha jaata hai
# Generator function allow us tto write a function that can send back a value and then later resume to pick up where it left off
# as storing a complete range function output into the list occupy the memory for that yield function comes so that it will not occupy what ever it required it will calculcate and give the output
# in below example jo output hoga wo complete list ko memory me save kar ke rakhega but yield function memory me save nahe rakhta bus wo formulla apne pass save rakhta hai
# jab jarurat ho tabhi formulla apply kr kaam chalu krta hai
# def create_cube(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result
#
# data =create_cube(10000000)
# print(data)




def create_cube(n):
    for x in range(n):
        yield x**3



for x in create_cube(100000):
    print(x)