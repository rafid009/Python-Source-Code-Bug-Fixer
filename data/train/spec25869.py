import numpy as np 

def function(x):

	b2 = 2
	x0 = x
	x = x
	paths = []
	try:
		if x <= 3:
			x = x+x0
			x = 5*5
			x = x/8
			paths.append(1)
		else:
			x = 0*x
			x0 = 3-3
			paths.append(2)
		if b2 > 7:
			b2 = 6-b2
			b2 = 5*b2
			x0 = b2+x
			paths.append(3)
		else:
			x0 = x0/3
			b2 = 6+b2
			b2 = 6/b2
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))