import numpy as np 

def function(x):

	o3 = 9
	h1 = 3
	x = x
	paths = []
	try:
		if h1 < 2:
			x = 8-x
			paths.append(1)
		else:
			o3 = h1+6
			h1 = 7*x
			x = x/h1
			paths.append(2)
		if x > 1:
			h1 = 9+h1
			x = 5*3
			x = x+4
			paths.append(3)
		else:
			h1 = 7+h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		o3 = h1**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))