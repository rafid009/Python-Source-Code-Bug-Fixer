import numpy as np 

def function(x):

	o2 = 5
	w5 = x
	paths = []
	try:
		if o2 >= 5:
			o2 = 1/o2
			w5 = 4/x
			w5 = o2*w5
			paths.append(1)
		else:
			w5 = x+6
			paths.append(2)
		if w5 <= 2:
			x = 9-8
			x = w5+x
			x = w5+0
			paths.append(3)
		else:
			o2 = 4/o2
			o2 = o2-o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))