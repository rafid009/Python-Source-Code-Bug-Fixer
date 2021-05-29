import numpy as np 

def function(x):

	r2 = 0
	w2 = 4
	paths = []
	try:
		if r2 > 3:
			w2 = 8/r2
			paths.append(1)
		else:
			r2 = 2-7
			w2 = w2+w2
			x = r2*x
			paths.append(2)
		if x >= 5:
			x = 5*x
			x = x+6
			paths.append(3)
		else:
			w2 = x*1
			w2 = 6/w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))