import numpy as np 

def function(x):

	a0 = x
	l0 = 7
	paths = []
	try:
		if x > 2:
			l0 = x+l0
			paths.append(1)
		else:
			a0 = a0/8
			l0 = l0+l0
			paths.append(2)
		if l0 < 9:
			a0 = x+1
			paths.append(3)
		else:
			a0 = x/9
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