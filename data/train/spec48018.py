import numpy as np 

def function(x):

	w8 = 8
	a6 = x
	paths = []
	try:
		if w8 >= 9:
			a6 = 5*a6
			x = 6/x
			w8 = a6/3
			paths.append(1)
		else:
			a6 = w8/x
			x = x/x
			paths.append(2)
		if x < 4:
			x = a6+3
			w8 = w8/w8
			x = 0-7
			paths.append(3)
		else:
			a6 = a6/a6
			w8 = w8/6
			x = a6/x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))