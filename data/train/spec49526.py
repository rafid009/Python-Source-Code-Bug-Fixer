import numpy as np 

def function(x):

	b6 = x
	i0 = x
	paths = []
	try:
		if x > 6:
			b6 = b6/6
			b6 = b6/b6
			paths.append(1)
		else:
			i0 = 9/2
			x = x*7
			x = x-2
			paths.append(2)
		if b6 >= 0:
			i0 = 1*5
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))