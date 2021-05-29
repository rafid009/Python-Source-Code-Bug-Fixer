import numpy as np 

def function(x):

	w8 = 6
	e1 = x
	x = x
	paths = []
	try:
		if w8 >= 1:
			x = 0/x
			e1 = e1*4
			paths.append(1)
		else:
			x = 2+x
			e1 = w8-7
			paths.append(2)
		if x < 6:
			x = x/9
			x = x*4
			x = 4-8
			paths.append(3)
		else:
			x = 0*e1
			w8 = w8-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))