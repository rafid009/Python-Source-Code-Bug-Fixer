import numpy as np 

def function(x):

	f3 = x
	h4 = 8
	paths = []
	try:
		if h4 > 0:
			h4 = h4/x
			f3 = f3+5
			paths.append(1)
		else:
			x = 5+x
			h4 = 4/x
			paths.append(2)
		if h4 > 3:
			x = x/2
			paths.append(3)
		else:
			f3 = 3*x
			x = 0*3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))