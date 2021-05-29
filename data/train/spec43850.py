import numpy as np 

def function(x):

	p8 = 5
	b2 = x
	paths = []
	try:
		if b2 < 3:
			x = x*9
			p8 = 3/8
			b2 = b2/5
			paths.append(1)
		else:
			x = x*4
			p8 = 6+p8
			paths.append(2)
		if b2 < 5:
			b2 = b2+8
			paths.append(3)
		else:
			b2 = 9+6
			b2 = 8/1
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