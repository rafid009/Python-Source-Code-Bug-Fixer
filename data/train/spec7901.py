import numpy as np 

def function(x):

	b9 = 5
	l4 = 7
	paths = []
	try:
		if x <= 5:
			x = x*b9
			x = x*6
			paths.append(1)
		else:
			l4 = l4-6
			paths.append(2)
		if l4 < 4:
			l4 = 7/l4
			b9 = b9/3
			paths.append(3)
		else:
			b9 = b9*b9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))