import numpy as np 

def function(x):

	w5 = 7
	h3 = 6
	paths = []
	try:
		if w5 <= 5:
			w5 = x*x
			paths.append(1)
		else:
			w5 = 5-h3
			x = h3+x
			paths.append(2)
		if h3 > 6:
			w5 = w5*h3
			w5 = 4-0
			h3 = x-h3
			paths.append(3)
		else:
			w5 = w5+w5
			w5 = w5*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))