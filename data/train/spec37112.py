import numpy as np 

def function(x):

	b2 = 8
	y4 = 4
	paths = []
	try:
		if b2 <= 5:
			b2 = x+b2
			paths.append(1)
		else:
			b2 = 0-b2
			paths.append(2)
		if b2 >= 6:
			x = 7-y4
			b2 = 3/6
			paths.append(3)
		else:
			x = 5-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))