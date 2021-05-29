import numpy as np 

def function(x):

	l4 = 8
	a0 = x
	paths = []
	try:
		if x >= 2:
			x = 2*x
			paths.append(1)
		else:
			x = l4*3
			paths.append(2)
		if l4 > 5:
			l4 = 4/l4
			a0 = 1+a0
			paths.append(3)
		else:
			l4 = l4+x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		l4 = a0**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))