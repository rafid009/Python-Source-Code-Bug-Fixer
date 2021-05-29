import numpy as np 

def function(x):

	l7 = x
	q0 = x
	paths = []
	try:
		if x > 0:
			q0 = q0/x
			q0 = 6+5
			q0 = 0-6
			paths.append(1)
		else:
			q0 = q0*l7
			x = x-2
			x = x+4
			paths.append(2)
		if l7 > 3:
			x = x/q0
			q0 = 2/q0
			paths.append(3)
		else:
			x = x*x
			l7 = l7*0
			l7 = 9/q0
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