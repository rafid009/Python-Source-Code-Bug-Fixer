import numpy as np 

def function(x):

	h2 = 2
	f5 = x
	paths = []
	try:
		if x > 8:
			h2 = 1-h2
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if x <= 1:
			h2 = h2+5
			paths.append(3)
		else:
			h2 = 0*x
			h2 = h2-6
			f5 = f5*x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))