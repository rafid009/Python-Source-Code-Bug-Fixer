import numpy as np 

def function(x):

	n2 = x
	b2 = x
	paths = []
	try:
		if n2 >= 0:
			b2 = b2*b2
			x = x*7
			x = n2*x
			paths.append(1)
		else:
			x = 8-3
			n2 = 1/n2
			paths.append(2)
		if b2 < 1:
			n2 = 8/n2
			paths.append(3)
		else:
			b2 = n2-2
			b2 = 5/7
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))