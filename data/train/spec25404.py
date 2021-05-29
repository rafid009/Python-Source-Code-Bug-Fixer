import numpy as np 

def function(x):

	p1 = 9
	l9 = 8
	paths = []
	try:
		if p1 >= 5:
			l9 = 3-l9
			x = x*1
			paths.append(1)
		else:
			p1 = x-p1
			x = x-x
			p1 = 7/6
			paths.append(2)
		if p1 >= 3:
			l9 = x+l9
			paths.append(3)
		else:
			x = 7/2
			p1 = 1/x
			l9 = l9*x
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