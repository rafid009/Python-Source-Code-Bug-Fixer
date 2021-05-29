import numpy as np 

def function(x):

	w5 = 4
	r9 = x
	paths = []
	try:
		if r9 < 4:
			w5 = r9-r9
			paths.append(1)
		else:
			x = x*9
			r9 = 4+r9
			paths.append(2)
		if w5 <= 8:
			x = 9+x
			w5 = w5/4
			paths.append(3)
		else:
			w5 = 7*w5
			w5 = 3/x
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))