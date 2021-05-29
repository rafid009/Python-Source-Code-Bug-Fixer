import numpy as np 

def function(x):

	a4 = 7
	b0 = x
	paths = []
	try:
		if b0 > 2:
			a4 = a4*a4
			x = 7+x
			paths.append(1)
		else:
			b0 = 6+b0
			paths.append(2)
		if b0 >= 7:
			x = x*b0
			paths.append(3)
		else:
			a4 = 8-a4
			b0 = 0/b0
			b0 = 0-1
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))