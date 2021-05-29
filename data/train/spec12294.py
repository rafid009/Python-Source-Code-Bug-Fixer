import numpy as np 

def function(x):

	l6 = 5
	b9 = x
	paths = []
	try:
		if l6 < 1:
			b9 = 3+b9
			paths.append(1)
		else:
			b9 = 6+b9
			l6 = l6*7
			paths.append(2)
		if x >= 7:
			x = b9/l6
			paths.append(3)
		else:
			l6 = 5-6
			l6 = 1+4
			l6 = l6*x
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