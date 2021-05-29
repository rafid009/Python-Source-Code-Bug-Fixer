import numpy as np 

def function(x):

	o5 = x
	u6 = x
	x = x
	paths = []
	try:
		if o5 <= 0:
			x = x+4
			paths.append(1)
		else:
			u6 = u6/6
			u6 = 8-u6
			paths.append(2)
		if x >= 4:
			u6 = 0/5
			u6 = o5+6
			paths.append(3)
		else:
			u6 = 2+u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))