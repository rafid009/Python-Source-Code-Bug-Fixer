import numpy as np 

def function(x):

	v8 = x
	w1 = 9
	paths = []
	try:
		if w1 > 3:
			w1 = 4/v8
			paths.append(1)
		else:
			v8 = v8/6
			paths.append(2)
		if x <= 1:
			w1 = v8*w1
			x = 2/v8
			x = x-0
			paths.append(3)
		else:
			w1 = 3/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))