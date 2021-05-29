import numpy as np 

def function(x):

	w2 = x
	y9 = 4
	paths = []
	try:
		if y9 <= 8:
			x = 3*x
			w2 = w2/4
			y9 = y9*1
			paths.append(1)
		else:
			y9 = y9/y9
			x = x+w2
			x = x/x
			paths.append(2)
		if w2 <= 9:
			y9 = y9/5
			paths.append(3)
		else:
			y9 = 7+x
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