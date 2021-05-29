import numpy as np 

def function(x):

	n3 = 3
	v8 = 9
	paths = []
	try:
		if v8 < 6:
			n3 = n3/5
			v8 = 2/x
			paths.append(1)
		else:
			x = x-v8
			v8 = 6-v8
			v8 = v8*4
			paths.append(2)
		if v8 > 3:
			n3 = 6/n3
			paths.append(3)
		else:
			x = 5-x
			v8 = v8*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))