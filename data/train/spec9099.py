import numpy as np 

def function(x):

	e7 = 5
	u5 = 9
	paths = []
	try:
		if e7 >= 3:
			u5 = 6-u5
			u5 = 4/u5
			x = 6-1
			paths.append(1)
		else:
			e7 = e7/u5
			paths.append(2)
		if x > 5:
			u5 = u5/5
			u5 = u5-u5
			e7 = x-e7
			paths.append(3)
		else:
			x = 3*u5
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))