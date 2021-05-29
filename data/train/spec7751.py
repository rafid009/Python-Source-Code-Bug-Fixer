import numpy as np 

def function(x):

	j9 = 0
	b8 = 3
	paths = []
	try:
		if b8 < 0:
			b8 = x+j9
			paths.append(1)
		else:
			b8 = b8-1
			b8 = 2+b8
			x = j9-b8
			paths.append(2)
		if x > 7:
			x = x*b8
			j9 = 8*3
			paths.append(3)
		else:
			b8 = 3-4
			j9 = j9*9
			j9 = j9-j9
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