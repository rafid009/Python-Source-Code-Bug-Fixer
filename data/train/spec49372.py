import numpy as np 

def function(x):

	r6 = 4
	w4 = 2
	paths = []
	try:
		if x < 6:
			r6 = r6/4
			r6 = r6/w4
			w4 = w4*x
			paths.append(1)
		else:
			r6 = 0*r6
			r6 = 8/x
			w4 = w4+6
			paths.append(2)
		if w4 >= 2:
			x = x-1
			x = 5*4
			paths.append(3)
		else:
			r6 = r6-9
			x = 1-0
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		w4 = r6**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))