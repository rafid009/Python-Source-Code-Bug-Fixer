import numpy as np 

def function(x):

	b1 = 6
	i7 = 0
	paths = []
	try:
		if x > 3:
			x = 9+x
			i7 = 7+b1
			paths.append(1)
		else:
			b1 = b1+x
			b1 = 3+x
			paths.append(2)
		if x >= 7:
			i7 = i7-9
			paths.append(3)
		else:
			i7 = i7*b1
			x = i7-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))