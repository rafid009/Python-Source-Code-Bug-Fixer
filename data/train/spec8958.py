import numpy as np 

def function(x):

	l6 = 7
	b3 = 8
	paths = []
	try:
		if x < 5:
			l6 = 3-8
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if b3 <= 3:
			l6 = 2+l6
			x = x-b3
			paths.append(3)
		else:
			b3 = b3+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))