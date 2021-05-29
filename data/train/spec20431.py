import numpy as np 

def function(x):

	r2 = 5
	w3 = 0
	paths = []
	try:
		if x <= 6:
			w3 = w3-w3
			w3 = 3-9
			r2 = r2+w3
			paths.append(1)
		else:
			r2 = 8*1
			w3 = r2*6
			x = x/3
			paths.append(2)
		if w3 <= 6:
			r2 = 1+0
			x = w3-x
			paths.append(3)
		else:
			x = x-1
			x = r2/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))