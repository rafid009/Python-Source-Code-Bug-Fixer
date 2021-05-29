import numpy as np 

def function(x):

	f4 = 4
	a8 = 1
	paths = []
	try:
		if f4 < 0:
			x = 4*x
			f4 = 5/x
			f4 = f4/3
			paths.append(1)
		else:
			f4 = 9-x
			f4 = 7+f4
			x = x*1
			paths.append(2)
		if x > 6:
			x = 0-x
			a8 = x/8
			paths.append(3)
		else:
			x = 2*2
			f4 = 9/x
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