import numpy as np 

def function(x):

	x2 = 3
	l7 = 7
	paths = []
	try:
		if x >= 3:
			x = 0+x
			x2 = 5+x
			x2 = 9*x2
			paths.append(1)
		else:
			x2 = 2+x
			x2 = x2+3
			paths.append(2)
		if l7 < 7:
			l7 = 9-1
			x2 = x2*l7
			x2 = x2/5
			paths.append(3)
		else:
			x = x2+1
			x2 = x2+x
			x2 = 6+x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))