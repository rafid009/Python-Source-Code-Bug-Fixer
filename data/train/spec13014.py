import numpy as np 

def function(x):

	f0 = x
	h1 = 4
	paths = []
	try:
		if h1 < 2:
			h1 = h1-4
			paths.append(1)
		else:
			h1 = 7-f0
			paths.append(2)
		if h1 > 3:
			x = f0*7
			x = 3-4
			h1 = 9/8
			paths.append(3)
		else:
			f0 = 1/7
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))