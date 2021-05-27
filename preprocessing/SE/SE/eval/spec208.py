import numpy as np 

def function(x):

	r6 = x
	v8 = 3
	paths = []
	try:
		if v8 <= 5:
			r6 = 8+r6
			v8 = 4+4
			x = 1-r6
			paths.append(1)
		else:
			v8 = 9-v8
			paths.append(2)
		if v8 >= 8:
			v8 = 0+x
			v8 = 8-x
			paths.append(3)
		else:
			x = r6-4
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