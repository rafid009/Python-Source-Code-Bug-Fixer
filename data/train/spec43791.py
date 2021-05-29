import numpy as np 

def function(x):

	x2 = 5
	b5 = x
	paths = []
	try:
		if x2 > 3:
			b5 = x2+4
			b5 = b5+x2
			b5 = b5/5
			paths.append(1)
		else:
			x2 = x/8
			b5 = 9/b5
			b5 = b5*6
			paths.append(2)
		if x < 5:
			b5 = 6/4
			x2 = 2+7
			paths.append(3)
		else:
			b5 = b5*4
			x2 = x2+2
			b5 = b5*x2
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