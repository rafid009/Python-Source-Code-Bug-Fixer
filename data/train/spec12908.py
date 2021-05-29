import numpy as np 

def function(x):

	b0 = 3
	u6 = x
	paths = []
	try:
		if x >= 8:
			u6 = 6/6
			paths.append(1)
		else:
			u6 = u6-6
			paths.append(2)
		if u6 <= 2:
			x = x*6
			b0 = 7*b0
			u6 = u6/u6
			paths.append(3)
		else:
			x = 9/x
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))