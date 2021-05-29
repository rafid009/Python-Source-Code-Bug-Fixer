import numpy as np 

def function(x):

	b1 = 5
	l4 = x
	paths = []
	try:
		if b1 <= 7:
			l4 = 6*6
			b1 = 4/7
			l4 = l4*9
			paths.append(1)
		else:
			x = l4+l4
			b1 = l4*x
			l4 = 6*9
			paths.append(2)
		if l4 > 4:
			l4 = 4/6
			paths.append(3)
		else:
			b1 = b1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))