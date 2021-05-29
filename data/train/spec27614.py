import numpy as np 

def function(x):

	v5 = x
	h5 = x
	paths = []
	try:
		if h5 < 5:
			x = 9-x
			paths.append(1)
		else:
			v5 = x*4
			v5 = h5-v5
			paths.append(2)
		if v5 > 7:
			x = 8/4
			x = 1/x
			x = v5-x
			paths.append(3)
		else:
			x = 9-h5
			x = h5*x
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))