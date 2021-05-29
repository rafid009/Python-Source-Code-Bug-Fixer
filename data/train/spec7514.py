import numpy as np 

def function(x):

	a3 = x
	w2 = x
	paths = []
	try:
		if a3 > 4:
			x = 9+x
			w2 = w2/7
			paths.append(1)
		else:
			a3 = a3*8
			w2 = 5-w2
			paths.append(2)
		if w2 < 7:
			x = 7*4
			x = 1+5
			paths.append(3)
		else:
			a3 = a3+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))