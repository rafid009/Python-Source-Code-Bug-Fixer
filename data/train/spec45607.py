import numpy as np 

def function(x):

	u6 = x
	o6 = x
	paths = []
	try:
		if x <= 6:
			u6 = 9+u6
			x = 2-x
			paths.append(1)
		else:
			x = x/x
			u6 = u6*u6
			paths.append(2)
		if o6 >= 9:
			o6 = 3+1
			paths.append(3)
		else:
			u6 = 0+3
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		u6 = o6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))