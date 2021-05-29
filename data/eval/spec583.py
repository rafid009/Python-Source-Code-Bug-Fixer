import numpy as np 

def function(x):

	w0 = 3
	r3 = x
	paths = []
	try:
		if w0 < 9:
			w0 = w0/1
			w0 = w0*x
			w0 = w0/w0
			paths.append(1)
		else:
			x = x-9
			w0 = w0/r3
			paths.append(2)
		if r3 < 8:
			x = 8/x
			x = r3*x
			paths.append(3)
		else:
			w0 = w0*0
			w0 = x*w0
			x = 5*3
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