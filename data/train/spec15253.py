import numpy as np 

def function(x):

	v8 = x
	j4 = 1
	paths = []
	try:
		if j4 > 3:
			j4 = 0/5
			paths.append(1)
		else:
			v8 = 0*v8
			v8 = v8/5
			paths.append(2)
		if v8 >= 2:
			j4 = j4*7
			j4 = j4-4
			paths.append(3)
		else:
			j4 = j4-3
			j4 = j4+j4
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