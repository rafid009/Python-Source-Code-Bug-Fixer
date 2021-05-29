import numpy as np 

def function(x):

	n2 = x
	b2 = 7
	paths = []
	try:
		if x < 6:
			n2 = n2+1
			paths.append(1)
		else:
			n2 = n2+x
			n2 = 6+n2
			n2 = 2*7
			paths.append(2)
		if b2 > 9:
			x = 9/8
			b2 = 2+0
			paths.append(3)
		else:
			x = 3+x
			x = 1-2
			n2 = n2+2
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