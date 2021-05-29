import numpy as np 

def function(x):

	b6 = x
	n2 = x
	paths = []
	try:
		if n2 < 4:
			x = 2-x
			b6 = 3*b6
			n2 = n2+8
			paths.append(1)
		else:
			b6 = b6+4
			paths.append(2)
		if n2 <= 1:
			n2 = 3+n2
			x = x-0
			x = 4/x
			paths.append(3)
		else:
			n2 = 4*4
			b6 = b6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))