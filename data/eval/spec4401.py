import numpy as np 

def function(x):

	z4 = x
	f4 = x
	paths = []
	try:
		if x >= 2:
			x = 1-x
			paths.append(1)
		else:
			x = 7*x
			x = z4-3
			paths.append(2)
		if z4 < 0:
			f4 = f4+1
			paths.append(3)
		else:
			x = 7*0
			f4 = f4-7
			f4 = 9/3
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