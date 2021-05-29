import numpy as np 

def function(x):

	w1 = 7
	l0 = x
	paths = []
	try:
		if x < 3:
			w1 = w1-8
			l0 = w1+5
			l0 = l0-8
			paths.append(1)
		else:
			x = 4*x
			l0 = 3/x
			x = x*w1
			paths.append(2)
		if x >= 5:
			w1 = 1+6
			x = w1+6
			paths.append(3)
		else:
			l0 = l0*5
			l0 = l0+2
			w1 = w1/3
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))