import numpy as np 

def function(x):

	l7 = x
	b0 = 7
	x = 0
	paths = []
	try:
		if l7 < 6:
			b0 = b0/7
			l7 = 3-7
			l7 = 8+l7
			paths.append(1)
		else:
			l7 = x-l7
			b0 = b0+x
			paths.append(2)
		if b0 < 7:
			x = x-1
			b0 = x*b0
			paths.append(3)
		else:
			b0 = 2+b0
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