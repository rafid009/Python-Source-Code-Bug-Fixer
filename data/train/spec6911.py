import numpy as np 

def function(x):

	l0 = x
	b3 = 6
	paths = []
	try:
		if b3 > 2:
			b3 = b3/l0
			b3 = 7*2
			b3 = b3+8
			paths.append(1)
		else:
			l0 = l0*b3
			l0 = 8*l0
			paths.append(2)
		if b3 >= 0:
			b3 = x+b3
			paths.append(3)
		else:
			l0 = l0/2
			l0 = 9-l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))