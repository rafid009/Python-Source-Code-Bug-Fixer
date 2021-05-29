import numpy as np 

def function(x):

	b3 = 2
	n6 = 0
	paths = []
	try:
		if b3 < 1:
			b3 = 9/4
			b3 = n6+b3
			paths.append(1)
		else:
			b3 = 4*1
			b3 = 1*x
			n6 = 3*7
			paths.append(2)
		if b3 <= 7:
			n6 = 8+x
			paths.append(3)
		else:
			n6 = 0*n6
			b3 = 2/x
			b3 = 2+6
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