import numpy as np 

def function(x):

	v3 = x
	v2 = x
	paths = []
	try:
		if v3 <= 9:
			v3 = v3/v2
			x = x*v3
			paths.append(1)
		else:
			v2 = v2+5
			x = 8/9
			v2 = 4+9
			paths.append(2)
		if v2 <= 9:
			v3 = 9/v2
			paths.append(3)
		else:
			v2 = 7/v2
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