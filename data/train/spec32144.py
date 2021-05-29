import numpy as np 

def function(x):

	l3 = x
	w0 = x
	paths = []
	try:
		if l3 > 6:
			x = x*7
			x = x/1
			paths.append(1)
		else:
			l3 = 9*l3
			x = w0-7
			w0 = 4+l3
			paths.append(2)
		if x > 5:
			l3 = 2/l3
			w0 = w0+3
			x = 3*x
			paths.append(3)
		else:
			l3 = 8*l3
			l3 = l3-1
			w0 = 2*x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))