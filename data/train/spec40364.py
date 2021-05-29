import numpy as np 

def function(x):

	u6 = x
	x0 = x
	paths = []
	try:
		if x0 <= 9:
			x = x*x
			x = x-9
			paths.append(1)
		else:
			u6 = 9-u6
			x = x-7
			paths.append(2)
		if x > 7:
			x = x-5
			x0 = x0+x0
			paths.append(3)
		else:
			u6 = u6/4
			u6 = u6+7
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x0 = u6**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))