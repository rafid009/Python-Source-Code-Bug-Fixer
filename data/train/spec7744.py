import numpy as np 

def function(x):

	x7 = 5
	v5 = 9
	paths = []
	try:
		if v5 >= 5:
			v5 = 5/v5
			x = x/3
			x7 = 9/x7
			paths.append(1)
		else:
			x = 1/x
			v5 = 4*8
			paths.append(2)
		if v5 < 8:
			x7 = x7+x
			paths.append(3)
		else:
			x7 = v5+9
			x7 = x7/4
			v5 = 4/8
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