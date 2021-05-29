import numpy as np 

def function(x):

	y3 = 9
	l7 = 4
	paths = []
	try:
		if l7 >= 8:
			l7 = x*1
			paths.append(1)
		else:
			l7 = 5/2
			paths.append(2)
		if l7 <= 1:
			y3 = 3*y3
			x = 3*x
			paths.append(3)
		else:
			y3 = 4+0
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