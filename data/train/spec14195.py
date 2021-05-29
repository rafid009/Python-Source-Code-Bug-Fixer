import numpy as np 

def function(x):

	l2 = x
	v1 = 1
	paths = []
	try:
		if x >= 8:
			l2 = l2*6
			v1 = v1+v1
			paths.append(1)
		else:
			x = x/8
			v1 = v1-7
			l2 = l2+l2
			paths.append(2)
		if l2 <= 0:
			l2 = 7/l2
			paths.append(3)
		else:
			v1 = 1+4
			l2 = 8+1
			l2 = l2+x
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