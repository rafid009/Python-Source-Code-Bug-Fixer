import numpy as np 

def function(x):

	b0 = x
	i5 = x
	paths = []
	try:
		if b0 > 5:
			b0 = b0-0
			x = x-3
			paths.append(1)
		else:
			x = b0*x
			b0 = b0-8
			b0 = 1-b0
			paths.append(2)
		if x < 4:
			x = x+6
			x = i5/b0
			paths.append(3)
		else:
			b0 = x/b0
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		b0 = i5**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))