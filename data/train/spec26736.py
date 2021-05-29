import numpy as np 

def function(x):

	h1 = 3
	v8 = x
	paths = []
	try:
		if x < 8:
			x = 5*x
			h1 = 1*h1
			paths.append(1)
		else:
			v8 = v8/x
			x = x/x
			v8 = h1*4
			paths.append(2)
		if x < 2:
			h1 = x/x
			paths.append(3)
		else:
			v8 = h1+v8
			h1 = 3-h1
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))