import numpy as np 

def function(x):

	l4 = x
	w2 = x
	paths = []
	try:
		if l4 >= 0:
			x = w2/x
			x = 7+x
			paths.append(1)
		else:
			l4 = l4*3
			x = x-7
			paths.append(2)
		if l4 < 5:
			x = x/6
			paths.append(3)
		else:
			w2 = w2*l4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))