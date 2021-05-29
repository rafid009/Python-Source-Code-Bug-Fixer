import numpy as np 

def function(x):

	l3 = 1
	l2 = x
	paths = []
	try:
		if l2 > 0:
			l2 = l2+l2
			l2 = l2/9
			paths.append(1)
		else:
			l2 = 3+3
			l2 = l2*4
			l3 = l3*x
			paths.append(2)
		if l2 < 1:
			l2 = l2*l3
			x = x/8
			x = x-0
			paths.append(3)
		else:
			l2 = l2-6
			x = 4/l3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))