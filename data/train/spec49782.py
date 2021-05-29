import numpy as np 

def function(x):

	b4 = 4
	g1 = x
	paths = []
	try:
		if b4 <= 5:
			g1 = g1*9
			x = 7-g1
			paths.append(1)
		else:
			g1 = 6/g1
			x = x-7
			b4 = b4*8
			paths.append(2)
		if g1 <= 2:
			g1 = 2+g1
			b4 = b4/7
			x = x*4
			paths.append(3)
		else:
			x = x/2
			b4 = b4-0
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