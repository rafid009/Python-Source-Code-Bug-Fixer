import numpy as np 

def function(x):

	g2 = 9
	b2 = 9
	paths = []
	try:
		if g2 < 6:
			x = x*b2
			b2 = b2+8
			paths.append(1)
		else:
			b2 = 5+b2
			paths.append(2)
		if x < 3:
			b2 = b2-g2
			paths.append(3)
		else:
			x = x+x
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