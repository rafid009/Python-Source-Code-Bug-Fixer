import numpy as np 

def function(x):

	l4 = 5
	w5 = 9
	paths = []
	try:
		if w5 >= 7:
			l4 = 2+l4
			w5 = 8-w5
			l4 = l4-2
			paths.append(1)
		else:
			w5 = 2*3
			l4 = l4+6
			x = l4-5
			paths.append(2)
		if w5 > 2:
			w5 = w5*8
			l4 = w5/x
			paths.append(3)
		else:
			l4 = l4*x
			l4 = w5-l4
			x = x/x
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