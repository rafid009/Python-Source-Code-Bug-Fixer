import numpy as np 

def function(x):

	u7 = 3
	o6 = 8
	paths = []
	try:
		if x < 6:
			u7 = 8*u7
			u7 = u7-1
			paths.append(1)
		else:
			x = 9*x
			o6 = 6*8
			paths.append(2)
		if o6 >= 7:
			u7 = u7/o6
			o6 = o6+x
			x = x-2
			paths.append(3)
		else:
			o6 = o6+8
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		u7 = o6**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))