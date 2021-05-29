import numpy as np 

def function(x):

	a7 = x
	b5 = x
	paths = []
	try:
		if b5 < 2:
			b5 = 9*x
			b5 = b5+x
			b5 = a7/b5
			paths.append(1)
		else:
			b5 = 0*6
			a7 = a7-4
			paths.append(2)
		if b5 <= 0:
			a7 = b5-b5
			paths.append(3)
		else:
			a7 = a7/3
			b5 = a7/9
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))