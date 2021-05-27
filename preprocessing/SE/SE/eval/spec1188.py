import numpy as np 

def function(x):

	a4 = x
	r9 = 2
	paths = []
	try:
		if x > 6:
			x = x*4
			x = r9+2
			paths.append(1)
		else:
			a4 = a4-a4
			x = x+8
			x = 4/x
			paths.append(2)
		if x >= 1:
			a4 = 1-a4
			paths.append(3)
		else:
			r9 = 6*9
			x = x-x
			x = 3*1
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))