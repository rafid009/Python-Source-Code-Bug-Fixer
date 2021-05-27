import numpy as np 

def function(x):

	r2 = x
	w5 = 7
	paths = []
	try:
		if r2 > 4:
			r2 = 0/w5
			w5 = x+2
			paths.append(1)
		else:
			w5 = 0-3
			w5 = 3+r2
			paths.append(2)
		if r2 >= 8:
			r2 = r2-w5
			x = 6-w5
			x = x+8
			paths.append(3)
		else:
			r2 = 4*r2
			r2 = r2/8
			w5 = w5*x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))