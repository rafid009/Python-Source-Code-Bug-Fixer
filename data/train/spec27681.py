import numpy as np 

def function(x):

	y0 = 8
	l7 = x
	paths = []
	try:
		if y0 >= 5:
			y0 = 3+x
			l7 = 9*l7
			paths.append(1)
		else:
			y0 = 6+9
			paths.append(2)
		if x <= 9:
			l7 = 2+l7
			l7 = 4+5
			paths.append(3)
		else:
			y0 = x+9
			l7 = 7-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))