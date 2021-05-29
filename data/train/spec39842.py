import numpy as np 

def function(x):

	b3 = x
	i7 = x
	paths = []
	try:
		if b3 >= 0:
			x = 3/x
			paths.append(1)
		else:
			b3 = x+x
			paths.append(2)
		if x < 0:
			i7 = i7*b3
			i7 = i7*5
			i7 = 2/i7
			paths.append(3)
		else:
			b3 = b3/1
			b3 = 8-b3
			x = 5-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))