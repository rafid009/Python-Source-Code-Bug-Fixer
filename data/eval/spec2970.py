import numpy as np 

def function(x):

	l7 = x
	k6 = x
	paths = []
	try:
		if k6 <= 2:
			k6 = k6-x
			paths.append(1)
		else:
			k6 = 2+0
			l7 = 4*l7
			paths.append(2)
		if l7 < 1:
			l7 = l7-7
			paths.append(3)
		else:
			x = k6-9
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