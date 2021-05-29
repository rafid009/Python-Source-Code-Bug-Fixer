import numpy as np 

def function(x):

	w2 = 6
	u0 = 2
	x = x
	paths = []
	try:
		if u0 < 0:
			w2 = w2+u0
			w2 = 8/2
			paths.append(1)
		else:
			x = x*7
			w2 = 7+6
			w2 = w2*5
			paths.append(2)
		if x > 6:
			x = x/x
			x = x+3
			u0 = u0-w2
			paths.append(3)
		else:
			w2 = 3-w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		u0 = w2**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))