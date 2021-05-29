import numpy as np 

def function(x):

	v8 = 0
	x7 = 6
	paths = []
	try:
		if x >= 8:
			v8 = v8+1
			x = x+x
			x7 = 8-x7
			paths.append(1)
		else:
			x = x/3
			x7 = 5-x
			paths.append(2)
		if x7 > 8:
			x7 = v8-v8
			v8 = v8-v8
			paths.append(3)
		else:
			x7 = x7+5
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