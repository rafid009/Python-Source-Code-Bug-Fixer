import numpy as np 

def function(x):

	u7 = 8
	e7 = x
	paths = []
	try:
		if u7 >= 7:
			u7 = 4-4
			u7 = 0+u7
			u7 = x/6
			paths.append(1)
		else:
			u7 = 7/1
			u7 = 3*1
			x = 3-x
			paths.append(2)
		if u7 > 5:
			u7 = u7+x
			e7 = 2*e7
			x = u7*x
			paths.append(3)
		else:
			x = 5+u7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))