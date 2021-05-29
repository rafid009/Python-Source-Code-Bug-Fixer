import numpy as np 

def function(x):

	a6 = 3
	v8 = x
	paths = []
	try:
		if v8 < 4:
			v8 = 8/4
			v8 = 6/5
			paths.append(1)
		else:
			x = 9-4
			paths.append(2)
		if x < 5:
			a6 = 1-2
			v8 = 8+v8
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))