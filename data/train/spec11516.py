import numpy as np 

def function(x):

	d5 = 8
	w3 = x
	x = 2
	paths = []
	try:
		if w3 >= 7:
			w3 = 2*x
			paths.append(1)
		else:
			d5 = d5/1
			x = 5*x
			w3 = w3/d5
			paths.append(2)
		if d5 < 9:
			x = w3+7
			x = 1*d5
			x = 0*x
			paths.append(3)
		else:
			w3 = 4-0
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		d5 = w3**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))