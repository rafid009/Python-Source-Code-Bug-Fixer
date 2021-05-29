import numpy as np 

def function(x):

	d1 = 4
	w7 = x
	paths = []
	try:
		if w7 >= 9:
			x = x+x
			w7 = 0*w7
			paths.append(1)
		else:
			x = x-d1
			w7 = w7-2
			w7 = 6+w7
			paths.append(2)
		if d1 <= 0:
			d1 = 5*d1
			x = w7+x
			paths.append(3)
		else:
			d1 = 4/d1
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		d1 = w7**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))