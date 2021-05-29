import numpy as np 

def function(x):

	b2 = 6
	a5 = 7
	paths = []
	try:
		if a5 <= 8:
			a5 = 2*x
			paths.append(1)
		else:
			b2 = b2+4
			a5 = a5*7
			x = b2/b2
			paths.append(2)
		if b2 <= 5:
			x = 2+x
			paths.append(3)
		else:
			a5 = a5/5
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