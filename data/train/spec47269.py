import numpy as np 

def function(x):

	u6 = x
	o6 = 5
	paths = []
	try:
		if o6 < 4:
			u6 = 1*8
			paths.append(1)
		else:
			o6 = o6*3
			x = o6*x
			paths.append(2)
		if x > 7:
			u6 = 6-o6
			o6 = 0+o6
			x = 3/x
			paths.append(3)
		else:
			x = x+u6
			x = 6-2
			u6 = u6*o6
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