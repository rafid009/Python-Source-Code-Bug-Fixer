import numpy as np 

def function(x):

	e2 = 1
	v5 = 8
	paths = []
	try:
		if v5 < 4:
			v5 = v5*4
			x = x/x
			paths.append(1)
		else:
			e2 = e2*v5
			x = 6/x
			paths.append(2)
		if v5 > 7:
			v5 = 0+v5
			paths.append(3)
		else:
			x = 7*8
			v5 = v5-v5
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