import numpy as np 

def function(x):

	r2 = 5
	f7 = x
	paths = []
	try:
		if r2 < 2:
			x = 2-6
			paths.append(1)
		else:
			x = r2/x
			paths.append(2)
		if x > 7:
			r2 = x+r2
			paths.append(3)
		else:
			r2 = r2-5
			x = 4+f7
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