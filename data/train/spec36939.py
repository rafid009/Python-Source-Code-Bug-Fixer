import numpy as np 

def function(x):

	v2 = 1
	x7 = x
	paths = []
	try:
		if x > 7:
			x7 = x7/x
			x = 5/x
			paths.append(1)
		else:
			x7 = x+4
			v2 = 8*v2
			paths.append(2)
		if x <= 8:
			v2 = 4-v2
			paths.append(3)
		else:
			x7 = x/1
			x7 = x*x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		v2 = x7**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))