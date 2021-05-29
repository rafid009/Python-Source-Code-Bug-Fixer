import numpy as np 

def function(x):

	l7 = x
	b4 = x
	paths = []
	try:
		if l7 > 2:
			x = x/3
			paths.append(1)
		else:
			l7 = l7-8
			x = x/x
			l7 = 7*b4
			paths.append(2)
		if l7 <= 7:
			b4 = 6-b4
			x = 5-6
			b4 = 3*l7
			paths.append(3)
		else:
			l7 = l7-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))