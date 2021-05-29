import numpy as np 

def function(x):

	w6 = 3
	o5 = 7
	x = x
	paths = []
	try:
		if w6 <= 0:
			x = 8-3
			o5 = o5*4
			o5 = o5-7
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if o5 >= 9:
			w6 = 7+w6
			x = 4-x
			paths.append(3)
		else:
			o5 = o5/o5
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