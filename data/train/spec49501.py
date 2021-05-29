import numpy as np 

def function(x):

	b9 = x
	t2 = 6
	paths = []
	try:
		if b9 > 4:
			b9 = t2/3
			x = x+4
			paths.append(1)
		else:
			b9 = b9-1
			paths.append(2)
		if b9 >= 5:
			b9 = 7*3
			x = x+8
			t2 = 8*b9
			paths.append(3)
		else:
			x = b9*x
			x = x+4
			x = 9+b9
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