import numpy as np 

def function(x):

	n0 = 1
	b9 = x
	paths = []
	try:
		if x <= 9:
			b9 = 9+b9
			x = x+x
			paths.append(1)
		else:
			x = x-n0
			b9 = x-b9
			paths.append(2)
		if n0 >= 5:
			b9 = x+9
			b9 = x/3
			x = 9*b9
			paths.append(3)
		else:
			x = x+1
			x = x-0
			x = x+9
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