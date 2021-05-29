import numpy as np 

def function(x):

	u5 = x
	g1 = 1
	paths = []
	try:
		if u5 >= 8:
			x = x-2
			paths.append(1)
		else:
			x = u5+0
			paths.append(2)
		if u5 >= 1:
			x = 5+g1
			u5 = 0+4
			u5 = u5-6
			paths.append(3)
		else:
			u5 = u5+2
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))