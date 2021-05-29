import numpy as np 

def function(x):

	w0 = x
	u3 = 7
	paths = []
	try:
		if w0 >= 3:
			x = 8-x
			paths.append(1)
		else:
			x = 7+4
			w0 = w0+2
			w0 = 9+w0
			paths.append(2)
		if w0 > 2:
			x = x-u3
			u3 = u3+0
			w0 = x*w0
			paths.append(3)
		else:
			x = x-2
			w0 = 4/x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		u3 = w0**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))