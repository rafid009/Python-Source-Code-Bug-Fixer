import numpy as np 

def function(x):

	l7 = x
	k6 = 3
	paths = []
	try:
		if k6 >= 0:
			x = k6/x
			k6 = k6*8
			x = k6*l7
			paths.append(1)
		else:
			k6 = k6-x
			paths.append(2)
		if x <= 2:
			l7 = l7+5
			paths.append(3)
		else:
			x = x+4
			x = 9*0
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