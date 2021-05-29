import numpy as np 

def function(x):

	d1 = x
	w6 = x
	paths = []
	try:
		if d1 < 5:
			w6 = 6*w6
			w6 = d1*w6
			paths.append(1)
		else:
			x = 3/5
			x = x*6
			paths.append(2)
		if w6 <= 7:
			w6 = 8-8
			d1 = d1/9
			x = x+0
			paths.append(3)
		else:
			x = x*x
			d1 = d1-w6
			d1 = 7*d1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))