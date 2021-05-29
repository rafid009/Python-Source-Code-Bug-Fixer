import numpy as np 

def function(x):

	x3 = x
	v5 = 5
	paths = []
	try:
		if x3 > 4:
			v5 = 8/9
			paths.append(1)
		else:
			v5 = 4+v5
			x = x3*x
			x3 = v5-x
			paths.append(2)
		if v5 < 9:
			v5 = v5-1
			paths.append(3)
		else:
			x = x-v5
			x3 = x3+6
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))