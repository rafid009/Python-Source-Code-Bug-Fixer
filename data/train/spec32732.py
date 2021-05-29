import numpy as np 

def function(x):

	u1 = 5
	w0 = x
	paths = []
	try:
		if w0 > 8:
			x = x*4
			w0 = 4/w0
			paths.append(1)
		else:
			u1 = u1+1
			paths.append(2)
		if u1 < 8:
			w0 = 4*w0
			u1 = u1*u1
			paths.append(3)
		else:
			w0 = w0/1
			u1 = 3*u1
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