import numpy as np 

def function(x):

	v6 = 7
	r2 = x
	paths = []
	try:
		if r2 <= 4:
			x = r2+x
			v6 = 0-v6
			x = v6-x
			paths.append(1)
		else:
			r2 = v6/r2
			x = r2+x
			paths.append(2)
		if x <= 4:
			r2 = v6*r2
			paths.append(3)
		else:
			v6 = v6-6
			v6 = 8/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))