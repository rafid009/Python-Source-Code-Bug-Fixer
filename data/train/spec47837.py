import numpy as np 

def function(x):

	w1 = 4
	v5 = x
	paths = []
	try:
		if w1 <= 3:
			x = 4+v5
			x = 3-x
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if v5 > 3:
			x = 3*v5
			v5 = 4*v5
			w1 = 8*6
			paths.append(3)
		else:
			w1 = x*x
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