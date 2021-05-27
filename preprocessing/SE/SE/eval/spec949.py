import numpy as np 

def function(x):

	l8 = 9
	p3 = x
	paths = []
	try:
		if p3 < 3:
			l8 = 4+l8
			l8 = l8-3
			paths.append(1)
		else:
			l8 = x*p3
			l8 = l8*5
			paths.append(2)
		if x > 4:
			l8 = 2-l8
			paths.append(3)
		else:
			l8 = l8*p3
			p3 = p3+p3
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))