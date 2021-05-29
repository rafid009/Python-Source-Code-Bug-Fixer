import numpy as np 

def function(x):

	i7 = 9
	b7 = 9
	paths = []
	try:
		if x > 5:
			i7 = i7/i7
			paths.append(1)
		else:
			i7 = b7/i7
			x = x-i7
			paths.append(2)
		if i7 < 3:
			i7 = i7/3
			b7 = b7-8
			b7 = b7-b7
			paths.append(3)
		else:
			b7 = 4*3
			x = 0/b7
			i7 = 3/i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))