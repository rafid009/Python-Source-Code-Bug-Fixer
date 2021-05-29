import numpy as np 

def function(x):

	h6 = 1
	f9 = 8
	paths = []
	try:
		if f9 >= 9:
			x = f9/8
			f9 = x*f9
			paths.append(1)
		else:
			f9 = h6/6
			x = x+2
			paths.append(2)
		if x >= 1:
			h6 = 2*h6
			paths.append(3)
		else:
			f9 = x-f9
			x = 2-x
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))