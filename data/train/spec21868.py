import numpy as np 

def function(x):

	w9 = x
	y9 = 7
	paths = []
	try:
		if x > 6:
			x = x*6
			w9 = w9*w9
			x = y9/x
			paths.append(1)
		else:
			w9 = w9/6
			x = x/y9
			paths.append(2)
		if w9 <= 3:
			x = x+8
			y9 = x/5
			x = x*3
			paths.append(3)
		else:
			y9 = w9/y9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w9 = w9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))