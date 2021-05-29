import numpy as np 

def function(x):

	r2 = 2
	v4 = 7
	paths = []
	try:
		if x >= 4:
			r2 = r2*9
			v4 = v4+0
			r2 = r2*4
			paths.append(1)
		else:
			r2 = r2/v4
			v4 = v4+3
			paths.append(2)
		if v4 < 4:
			r2 = 2+r2
			v4 = 9+4
			paths.append(3)
		else:
			v4 = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))