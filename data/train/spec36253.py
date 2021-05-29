import numpy as np 

def function(x):

	l8 = 8
	w5 = 8
	paths = []
	try:
		if x <= 5:
			w5 = 3*4
			w5 = w5*2
			l8 = 7/l8
			paths.append(1)
		else:
			w5 = l8+w5
			paths.append(2)
		if w5 <= 3:
			x = 8+w5
			w5 = x/6
			w5 = w5*6
			paths.append(3)
		else:
			l8 = 2+5
			w5 = w5+x
			l8 = l8/7
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