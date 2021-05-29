import numpy as np 

def function(x):

	x2 = x
	w9 = x
	paths = []
	try:
		if w9 >= 6:
			x = x+x2
			x = x+5
			w9 = 7*x
			paths.append(1)
		else:
			w9 = 4-w9
			x2 = x2/w9
			paths.append(2)
		if x2 < 6:
			x2 = x/7
			w9 = 7+5
			paths.append(3)
		else:
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))