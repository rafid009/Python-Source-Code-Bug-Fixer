import numpy as np 

def function(x):

	k4 = 0
	e5 = x
	x = x
	paths = []
	try:
		if x >= 9:
			e5 = 7-x
			paths.append(1)
		else:
			e5 = e5*2
			k4 = 1+6
			k4 = x*4
			paths.append(2)
		if k4 >= 9:
			x = x*5
			k4 = k4*1
			paths.append(3)
		else:
			k4 = k4+5
			k4 = 9*k4
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))