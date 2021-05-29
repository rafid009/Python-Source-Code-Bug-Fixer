import numpy as np 

def function(x):

	h5 = x
	v5 = x
	paths = []
	try:
		if v5 > 3:
			x = 5/v5
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if h5 > 0:
			h5 = 7-4
			v5 = 2+v5
			paths.append(3)
		else:
			v5 = v5-6
			x = x/h5
			v5 = v5*7
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))