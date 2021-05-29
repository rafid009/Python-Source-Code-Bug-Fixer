import numpy as np 

def function(x):

	o8 = 7
	w1 = x
	x = 1
	paths = []
	try:
		if x >= 9:
			w1 = 7*w1
			x = o8/o8
			paths.append(1)
		else:
			x = 0-7
			paths.append(2)
		if o8 <= 5:
			o8 = w1*8
			o8 = o8-3
			paths.append(3)
		else:
			w1 = 4/w1
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))