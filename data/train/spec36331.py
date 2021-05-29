import numpy as np 

def function(x):

	k1 = x
	v8 = x
	paths = []
	try:
		if v8 > 7:
			x = x-8
			paths.append(1)
		else:
			v8 = v8*7
			paths.append(2)
		if x > 3:
			k1 = v8-k1
			x = v8+x
			paths.append(3)
		else:
			v8 = v8/x
			v8 = k1/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))