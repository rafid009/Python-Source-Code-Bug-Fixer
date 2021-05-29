import numpy as np 

def function(x):

	w4 = 5
	d5 = 6
	paths = []
	try:
		if w4 <= 1:
			d5 = d5*2
			w4 = 4/w4
			paths.append(1)
		else:
			d5 = d5+5
			d5 = d5-d5
			d5 = w4+d5
			paths.append(2)
		if x < 8:
			w4 = w4*w4
			d5 = x-d5
			paths.append(3)
		else:
			w4 = w4-4
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