import numpy as np 

def function(x):

	o7 = 2
	w7 = x
	paths = []
	try:
		if w7 < 1:
			o7 = 9*9
			w7 = 8+1
			paths.append(1)
		else:
			w7 = 3-4
			w7 = w7+4
			paths.append(2)
		if x >= 3:
			o7 = o7*w7
			paths.append(3)
		else:
			o7 = 1+w7
			o7 = o7/9
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))