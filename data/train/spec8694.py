import numpy as np 

def function(x):

	x2 = x
	b2 = 6
	paths = []
	try:
		if b2 > 5:
			x2 = x2/5
			b2 = x2+4
			paths.append(1)
		else:
			x = 5/x2
			x2 = x2-x2
			paths.append(2)
		if x < 1:
			x2 = x-x2
			b2 = x2*x
			b2 = 1/1
			paths.append(3)
		else:
			b2 = 0*b2
			b2 = b2/7
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))