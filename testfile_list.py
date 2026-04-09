from loguru import *
import math
#list can contain string,number,boolean
carlist=['tata','honda','toyota','suzuki','vw','skoda']
#positive index
logger.info(f"my fav car brand is {carlist[1]}")
#negetive index
logger.info(f"my 2nd fav car brand is {carlist[-1]}")

###########################################
# list.append
# list.insert
# list.extend   or  List1+List2
###########################################

#list.append("xyz")  adding value to list
carlist.append("mahindra")
logger.info(f"updated list is : {carlist}")
#list.insert(0,"xyz")  adding a new value at particular index
#list.insert(index,"new value")
carlist.insert(0,"chevrolet")
logger.info(f"updated list is : {carlist}")
#list.extend  .... adding new list to existing list 
cc=[1000,1500,2000]
carlist.extend(cc)
logger.info(f"updated list is : {carlist}")

# car2=carlist.extend(cc)  ##### here changes are hold in carlist variable itself
# print(car2)  this will return null value
''' In Python, list.extend() is an in-place operation.
That means it directly modifies the list you call it on (carlist), rather than creating and returning a new list.
Because the list is already updated, Python doesn’t need to return anything useful. So, by design, extend() returns None.'''


#multi-dimensional list

carlist_cc=[['tata',1500],['honda',2000],['toyota',1300],['suzuki',1800],['vw',1000],['skoda',1500]]
logger.info(f"{carlist_cc[0][0]} has cubic capacity of {carlist_cc[0][1]}")

##### to reverse a string
logger.info(carlist)
logger.info(carlist[::-1])

len(carlist)

