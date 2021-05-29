import numpy as np 

def function(x):

	w0 = 8
	r3 = 1
	paths = []
	try:
		if w0 >= 3:
			x = x*7
			paths.append(1)
		else:
			w0 = w0+6
			x = 1+x
			w0 = 8*x
			paths.append(2)
		if x <= 7:
			r3 = r3-4
			x = 7-x
			r3 = r3/8
			paths.append(3)
		else:
			w0 = w0-0
			x = 0+1
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))