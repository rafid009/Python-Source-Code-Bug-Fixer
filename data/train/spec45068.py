import numpy as np 

def function(x):

	w2 = x
	x4 = x
	paths = []
	try:
		if x4 < 2:
			x = x*3
			paths.append(1)
		else:
			x = x-1
			x = x*x
			paths.append(2)
		if x4 <= 2:
			x4 = 4+x4
			w2 = w2/8
			x = w2-5
			paths.append(3)
		else:
			w2 = w2+x4
			x = x*x4
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))