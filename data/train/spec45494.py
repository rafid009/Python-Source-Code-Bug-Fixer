import numpy as np 

def function(x):

	a5 = 9
	e4 = x
	paths = []
	try:
		if e4 <= 1:
			e4 = 8/e4
			x = 0-5
			e4 = e4+8
			paths.append(1)
		else:
			e4 = 1/x
			x = 7/x
			x = x+6
			paths.append(2)
		if e4 > 7:
			a5 = 2*1
			paths.append(3)
		else:
			e4 = e4*e4
			a5 = 2-a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))