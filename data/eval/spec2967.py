import numpy as np 

def function(x):

	w1 = x
	d5 = 4
	paths = []
	try:
		if d5 <= 9:
			d5 = d5*x
			x = w1/x
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if w1 < 6:
			d5 = d5+d5
			w1 = 6*w1
			w1 = w1/1
			paths.append(3)
		else:
			x = 8*x
			x = x-4
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))