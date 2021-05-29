import numpy as np 

def function(x):

	w2 = 9
	o3 = 8
	x = x
	paths = []
	try:
		if x <= 3:
			x = x/7
			o3 = x-9
			paths.append(1)
		else:
			x = 1-w2
			w2 = 0-x
			w2 = o3-w2
			paths.append(2)
		if w2 >= 0:
			o3 = o3-o3
			w2 = 7*o3
			w2 = o3*5
			paths.append(3)
		else:
			x = x-9
			o3 = 2/o3
			w2 = w2/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))