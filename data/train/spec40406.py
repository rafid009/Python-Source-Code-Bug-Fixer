import numpy as np 

def function(x):

	k5 = 6
	b6 = x
	x = x
	paths = []
	try:
		if b6 > 9:
			k5 = k5+8
			x = b6*x
			k5 = 5/b6
			paths.append(1)
		else:
			k5 = 2+6
			x = x/k5
			paths.append(2)
		if b6 >= 7:
			x = x-4
			b6 = 4/2
			paths.append(3)
		else:
			k5 = k5+x
			x = b6/b6
			x = x*3
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