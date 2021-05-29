import numpy as np 

def function(x):

	u3 = x
	w0 = 1
	paths = []
	try:
		if x <= 5:
			w0 = w0-9
			paths.append(1)
		else:
			x = 9+x
			u3 = 6+u3
			paths.append(2)
		if x > 6:
			w0 = u3+1
			x = 3-u3
			w0 = 9*w0
			paths.append(3)
		else:
			w0 = w0/4
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))