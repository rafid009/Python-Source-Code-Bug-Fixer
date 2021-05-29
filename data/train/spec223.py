import numpy as np 

def function(x):

	o0 = 7
	j1 = 4
	paths = []
	try:
		if o0 < 4:
			o0 = 7-3
			j1 = j1/7
			paths.append(1)
		else:
			j1 = j1*8
			j1 = 0/j1
			paths.append(2)
		if x >= 0:
			j1 = 3-j1
			x = 5-x
			paths.append(3)
		else:
			x = x+5
			x = o0/x
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