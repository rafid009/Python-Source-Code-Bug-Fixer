import numpy as np 

def function(x):

	o9 = x
	w6 = 0
	paths = []
	try:
		if w6 > 7:
			o9 = 7/3
			w6 = x+1
			paths.append(1)
		else:
			w6 = x-w6
			x = 6-x
			x = w6-6
			paths.append(2)
		if o9 <= 1:
			o9 = o9*0
			x = o9-8
			x = x+2
			paths.append(3)
		else:
			o9 = o9*w6
			w6 = w6-x
			w6 = w6*w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))