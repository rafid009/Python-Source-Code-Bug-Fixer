import numpy as np 

def function(x):

	l1 = 1
	v4 = 7
	paths = []
	try:
		if l1 > 5:
			l1 = 1/2
			paths.append(1)
		else:
			v4 = v4+8
			paths.append(2)
		if x < 2:
			l1 = 8-l1
			l1 = l1+v4
			x = v4*x
			paths.append(3)
		else:
			v4 = 5+5
			l1 = x-7
			l1 = l1*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))