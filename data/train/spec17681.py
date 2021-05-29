import numpy as np 

def function(x):

	l0 = x
	w1 = 5
	paths = []
	try:
		if l0 <= 2:
			x = x*x
			x = 9-w1
			paths.append(1)
		else:
			l0 = l0-6
			paths.append(2)
		if w1 >= 5:
			l0 = l0+w1
			x = l0/x
			paths.append(3)
		else:
			l0 = l0*8
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		w1 = l0**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))