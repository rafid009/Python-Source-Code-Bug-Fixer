import numpy as np 

def function(x):

	v1 = 1
	l7 = 8
	paths = []
	try:
		if l7 <= 8:
			v1 = 8-l7
			x = x-2
			v1 = x+0
			paths.append(1)
		else:
			x = 4+l7
			v1 = 8*4
			x = 5+x
			paths.append(2)
		if l7 < 0:
			x = 6-x
			paths.append(3)
		else:
			l7 = 8+v1
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))