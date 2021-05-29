import numpy as np 

def function(x):

	f2 = 2
	u6 = x
	paths = []
	try:
		if x < 7:
			u6 = u6/5
			paths.append(1)
		else:
			f2 = 4/f2
			paths.append(2)
		if f2 >= 1:
			u6 = 3/u6
			f2 = 5+f2
			u6 = u6/2
			paths.append(3)
		else:
			u6 = 4*4
			u6 = 7+u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))