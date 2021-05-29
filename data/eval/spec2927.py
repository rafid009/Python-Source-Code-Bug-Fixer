import numpy as np 

def function(x):

	k1 = x
	v8 = 9
	paths = []
	try:
		if v8 >= 6:
			v8 = v8*4
			k1 = 1-k1
			paths.append(1)
		else:
			k1 = k1*v8
			v8 = 5+v8
			paths.append(2)
		if k1 > 5:
			v8 = 6*v8
			paths.append(3)
		else:
			v8 = v8*x
			k1 = k1-9
			v8 = v8+1
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