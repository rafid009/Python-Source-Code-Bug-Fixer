import numpy as np 

def function(x):

	v3 = 5
	w5 = x
	paths = []
	try:
		if x > 0:
			v3 = v3+9
			paths.append(1)
		else:
			x = 5/w5
			v3 = 4-v3
			v3 = v3*7
			paths.append(2)
		if v3 < 7:
			v3 = 3/x
			x = 1-x
			x = v3*x
			paths.append(3)
		else:
			v3 = 7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))