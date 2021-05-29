import numpy as np 

def function(x):

	d2 = 8
	w5 = 5
	paths = []
	try:
		if d2 < 1:
			w5 = w5/9
			x = 5*6
			paths.append(1)
		else:
			d2 = d2-w5
			w5 = d2+w5
			d2 = d2+d2
			paths.append(2)
		if w5 <= 3:
			x = 4-x
			x = 2*x
			x = 1-d2
			paths.append(3)
		else:
			d2 = w5-d2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))