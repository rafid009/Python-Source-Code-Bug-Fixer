import numpy as np 

def function(x):

	o5 = x
	w7 = x
	paths = []
	try:
		if w7 <= 1:
			x = x+6
			w7 = x+4
			paths.append(1)
		else:
			x = x-5
			o5 = 5/5
			x = x-w7
			paths.append(2)
		if w7 > 3:
			o5 = o5-2
			paths.append(3)
		else:
			w7 = w7/6
			w7 = 6+w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))