import numpy as np 

def function(x):

	w2 = 5
	d1 = x
	paths = []
	try:
		if w2 > 0:
			d1 = w2/3
			d1 = 2+6
			d1 = 0/d1
			paths.append(1)
		else:
			d1 = w2-2
			d1 = 0+d1
			paths.append(2)
		if w2 >= 5:
			w2 = d1-8
			w2 = w2/5
			paths.append(3)
		else:
			w2 = d1*w2
			x = 3*w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))