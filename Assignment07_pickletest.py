# ------------------------------------------------- #
# Title: pickletest.py
# Description: trying to figure pickling out
# ChangeLog: (Who, When, What)
# KHarms,8.20.2023,created script
# ------------------------------------------------- #
import pickle

# create data object -- this is a dictionary
dic_obj = {1: "The Lovecats", 2: "Boys Don't Cry", 3: "A Night Like This"}
print(dic_obj)
print(type(dic_obj))  # data type

# save data to file using pickle.dump method
test_file = open('test_data.dat', 'wb')  # open file in write binary mode
pickle.dump(dic_obj, test_file)  # put dic_obj in file
print('\n*Pickled*\n')
test_file.close()  # close the file

# read data from file using pickle.load method
test_file = open('test_data.dat', 'rb')  # open file in read binary mode
data = pickle.load(test_file)  # get the pickled object from the file

# here is our object again!
print('Un-pickled!')
print(data)
print(type(data))  # data type of original object is preserved
