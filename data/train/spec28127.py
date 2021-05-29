import numpy as np 

def function(x):

	p9 = 9
	w4 = 4
	paths = []
	try:
		if x < 1:
			w4 = 1*5
			p9 = 7-6
			w4 = 5*w4
			paths.append(1)
		else:
			x = 3+x
			x = 9/7
			w4 = 4*w4
			paths.append(2)
		if p9 < 0:
			w4 = p9-9
			paths.append(3)
		else:
			w4 = w4-4
			p9 = x-p9
			w4 = w4*w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))