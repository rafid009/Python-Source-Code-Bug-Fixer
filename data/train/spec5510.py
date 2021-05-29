import numpy as np 

def function(x):

	b3 = 5
	b9 = 2
	paths = []
	try:
		if b3 > 4:
			b9 = 6+5
			paths.append(1)
		else:
			b3 = b3*x
			paths.append(2)
		if b3 >= 2:
			b9 = 8-b9
			paths.append(3)
		else:
			b9 = 6*6
			b9 = 1+b9
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