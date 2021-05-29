import numpy as np 

def function(x):

	r9 = x
	u5 = x
	x = 8
	paths = []
	try:
		if x < 8:
			u5 = 7/6
			x = 1-x
			r9 = r9*0
			paths.append(1)
		else:
			x = 1-0
			paths.append(2)
		if x >= 9:
			u5 = 2*u5
			u5 = 8/u5
			paths.append(3)
		else:
			r9 = r9+6
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		r9 = u5**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))