import numpy as np 

def function(x):

	b1 = x
	x1 = x
	paths = []
	try:
		if b1 <= 2:
			x = b1-2
			b1 = x+1
			b1 = b1+0
			paths.append(1)
		else:
			b1 = 6+x
			x = 1/3
			paths.append(2)
		if x1 <= 8:
			b1 = b1+5
			paths.append(3)
		else:
			b1 = 7/4
			x1 = x1+1
			b1 = b1+x1
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