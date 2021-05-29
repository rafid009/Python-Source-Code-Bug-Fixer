import numpy as np 

def function(x):

	r5 = 7
	u7 = 7
	paths = []
	try:
		if u7 >= 1:
			u7 = 9*5
			x = 9*x
			paths.append(1)
		else:
			u7 = u7+5
			u7 = u7/8
			u7 = 0/x
			paths.append(2)
		if x < 5:
			x = 6+2
			paths.append(3)
		else:
			x = x-7
			r5 = 8/r5
			r5 = 1*r5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))