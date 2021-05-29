import numpy as np 

def function(x):

	q9 = 5
	b1 = 3
	x = x
	paths = []
	try:
		if x <= 6:
			b1 = 2+x
			b1 = 5-b1
			b1 = 9-b1
			paths.append(1)
		else:
			b1 = x-x
			paths.append(2)
		if b1 < 0:
			b1 = x*q9
			b1 = b1-0
			q9 = 9+q9
			paths.append(3)
		else:
			b1 = 7+b1
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