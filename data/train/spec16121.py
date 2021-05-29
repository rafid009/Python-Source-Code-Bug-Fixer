import numpy as np 

def function(x):

	x7 = x
	v3 = x
	paths = []
	try:
		if x7 >= 3:
			x7 = 1/7
			x = x+x
			paths.append(1)
		else:
			v3 = 6+v3
			v3 = v3-2
			v3 = 6/v3
			paths.append(2)
		if v3 < 5:
			x7 = 7*x7
			x7 = 2+x7
			x7 = v3+3
			paths.append(3)
		else:
			v3 = 7-v3
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		v3 = x7**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))