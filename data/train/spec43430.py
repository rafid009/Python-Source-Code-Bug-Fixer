import numpy as np 

def function(x):

	b8 = x
	a2 = x
	x = 1
	paths = []
	try:
		if a2 <= 5:
			a2 = b8*a2
			paths.append(1)
		else:
			x = x-7
			a2 = a2*a2
			paths.append(2)
		if x > 7:
			a2 = 4-1
			paths.append(3)
		else:
			x = 4-6
			b8 = 0/b8
			a2 = 0*b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))