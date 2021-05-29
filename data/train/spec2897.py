import numpy as np 

def function(x):

	h8 = x
	v5 = 7
	paths = []
	try:
		if x >= 1:
			v5 = 9+v5
			x = x*x
			paths.append(1)
		else:
			x = x/5
			x = 5-v5
			paths.append(2)
		if h8 <= 4:
			x = 4/h8
			x = 1+x
			paths.append(3)
		else:
			h8 = h8/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))