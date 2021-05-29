import numpy as np 

def function(x):

	b2 = x
	j9 = x
	paths = []
	try:
		if b2 <= 3:
			j9 = b2*7
			j9 = 0*j9
			paths.append(1)
		else:
			x = 6+8
			paths.append(2)
		if x < 2:
			j9 = j9*x
			b2 = b2+6
			b2 = b2-2
			paths.append(3)
		else:
			x = 7-6
			j9 = 1+9
			x = j9/8
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