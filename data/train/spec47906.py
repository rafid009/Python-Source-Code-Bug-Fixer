import numpy as np 

def function(x):

	w6 = 1
	u5 = x
	paths = []
	try:
		if x <= 8:
			u5 = 1-u5
			u5 = u5-1
			x = 0/x
			paths.append(1)
		else:
			w6 = w6+6
			w6 = 4-1
			paths.append(2)
		if x <= 6:
			u5 = u5-0
			paths.append(3)
		else:
			x = 7/w6
			w6 = 3-1
			u5 = u5*x
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))