import numpy as np 

def function(x):

	g4 = x
	b1 = 4
	paths = []
	try:
		if x <= 6:
			b1 = 1/g4
			b1 = b1/7
			b1 = g4+b1
			paths.append(1)
		else:
			b1 = g4/g4
			paths.append(2)
		if b1 <= 9:
			b1 = b1/8
			paths.append(3)
		else:
			x = 7*7
			g4 = b1+0
			g4 = b1*1
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