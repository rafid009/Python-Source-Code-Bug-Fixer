import numpy as np 

def function(x):

	w2 = 7
	l4 = x
	paths = []
	try:
		if x >= 0:
			w2 = x+l4
			w2 = 0-2
			paths.append(1)
		else:
			w2 = w2-6
			x = 2/7
			paths.append(2)
		if x < 4:
			w2 = w2/5
			w2 = 4/l4
			l4 = 6+l4
			paths.append(3)
		else:
			w2 = l4-w2
			l4 = l4/l4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))