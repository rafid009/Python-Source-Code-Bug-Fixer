import numpy as np 

def function(x):

	o5 = 5
	w1 = x
	paths = []
	try:
		if o5 < 4:
			w1 = w1*8
			x = x*4
			paths.append(1)
		else:
			x = 2*x
			w1 = 8/w1
			paths.append(2)
		if w1 < 2:
			o5 = o5*3
			paths.append(3)
		else:
			o5 = x/o5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))