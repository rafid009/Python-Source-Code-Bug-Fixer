import numpy as np 

def function(x):

	v8 = x
	w3 = 6
	paths = []
	try:
		if x < 9:
			x = x-6
			v8 = x+7
			paths.append(1)
		else:
			v8 = v8/v8
			x = 8*x
			paths.append(2)
		if w3 >= 8:
			x = x-v8
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))