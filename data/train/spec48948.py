import numpy as np 

def function(x):

	o6 = x
	u6 = x
	paths = []
	try:
		if x < 3:
			x = x+u6
			paths.append(1)
		else:
			u6 = u6-7
			x = x-6
			paths.append(2)
		if u6 < 1:
			o6 = u6-u6
			o6 = u6/6
			u6 = u6+9
			paths.append(3)
		else:
			x = x+6
			o6 = o6*o6
			x = 8/o6
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