import numpy as np 

def function(x):

	b9 = 5
	i7 = 8
	paths = []
	try:
		if x > 2:
			x = 1-x
			paths.append(1)
		else:
			b9 = b9-5
			paths.append(2)
		if x >= 4:
			x = x*i7
			b9 = b9-b9
			paths.append(3)
		else:
			i7 = i7*i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))