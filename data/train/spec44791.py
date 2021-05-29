import numpy as np 

def function(x):

	o6 = 1
	u6 = x
	paths = []
	try:
		if o6 > 3:
			x = x-x
			paths.append(1)
		else:
			o6 = 6-o6
			o6 = o6+u6
			paths.append(2)
		if o6 > 2:
			u6 = o6-x
			x = o6/x
			o6 = o6/o6
			paths.append(3)
		else:
			o6 = o6/o6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		o6 = u6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))