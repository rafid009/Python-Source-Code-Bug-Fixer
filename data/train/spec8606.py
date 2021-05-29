import numpy as np 

def function(x):

	v8 = x
	b9 = 8
	x = 3
	paths = []
	try:
		if v8 <= 6:
			v8 = v8/b9
			v8 = b9-v8
			v8 = 2-v8
			paths.append(1)
		else:
			b9 = x/b9
			x = 1+x
			b9 = b9/v8
			paths.append(2)
		if x <= 6:
			x = x-v8
			paths.append(3)
		else:
			v8 = v8+1
			x = 4+2
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