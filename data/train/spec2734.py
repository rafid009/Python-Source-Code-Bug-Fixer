import numpy as np 

def function(x):

	u4 = x
	j1 = x
	paths = []
	try:
		if j1 > 3:
			j1 = j1/4
			x = 6-6
			paths.append(1)
		else:
			u4 = u4/3
			x = 0/j1
			paths.append(2)
		if u4 > 6:
			u4 = 6*j1
			u4 = u4+0
			paths.append(3)
		else:
			x = 4+3
			x = x-4
			j1 = x+7
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))