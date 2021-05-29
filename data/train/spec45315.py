import numpy as np 

def function(x):

	x4 = x
	e2 = x
	paths = []
	try:
		if x < 3:
			x = 0+x4
			paths.append(1)
		else:
			x = 5*x
			x = 8-3
			x = x*7
			paths.append(2)
		if e2 <= 4:
			x = x/x4
			paths.append(3)
		else:
			x4 = x4+x4
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))