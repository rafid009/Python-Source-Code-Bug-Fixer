import numpy as np 

def function(x):

	y8 = 2
	u6 = x
	paths = []
	try:
		if u6 < 8:
			y8 = x*y8
			y8 = 7*9
			u6 = y8+u6
			paths.append(1)
		else:
			u6 = u6+6
			paths.append(2)
		if x > 2:
			x = x+y8
			u6 = 5/x
			y8 = 3*2
			paths.append(3)
		else:
			y8 = y8+7
			u6 = u6/7
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