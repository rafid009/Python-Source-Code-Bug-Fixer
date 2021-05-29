import numpy as np 

def function(x):

	w1 = x
	u6 = x
	paths = []
	try:
		if x < 3:
			u6 = 6+u6
			x = x+5
			paths.append(1)
		else:
			x = x*7
			w1 = 0*6
			x = x-9
			paths.append(2)
		if x >= 2:
			u6 = x/u6
			paths.append(3)
		else:
			x = x+7
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