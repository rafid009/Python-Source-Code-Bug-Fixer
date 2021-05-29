import numpy as np 

def function(x):

	x8 = 0
	w3 = x
	paths = []
	try:
		if w3 < 9:
			x8 = 4+5
			x = x/x8
			w3 = 6+x8
			paths.append(1)
		else:
			w3 = 2/3
			paths.append(2)
		if w3 >= 5:
			w3 = w3+2
			x = x*6
			paths.append(3)
		else:
			w3 = 4/w3
			x8 = 7*4
			x = x8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))