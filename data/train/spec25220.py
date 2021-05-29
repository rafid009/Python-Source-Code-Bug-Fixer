import numpy as np 

def function(x):

	y6 = 6
	l2 = x
	paths = []
	try:
		if y6 > 3:
			y6 = 6*l2
			paths.append(1)
		else:
			l2 = 0+l2
			x = x*5
			paths.append(2)
		if l2 > 3:
			x = x+4
			paths.append(3)
		else:
			x = l2-7
			y6 = 1+y6
			l2 = 6+l2
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		l2 = y6**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))