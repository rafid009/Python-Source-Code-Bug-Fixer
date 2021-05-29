import numpy as np 

def function(x):

	b9 = x
	b1 = x
	paths = []
	try:
		if b1 >= 4:
			b9 = b9*0
			b9 = 5+b1
			paths.append(1)
		else:
			b1 = b1/b9
			paths.append(2)
		if b9 >= 3:
			b9 = 8+b9
			x = 5+b9
			x = 8-4
			paths.append(3)
		else:
			b9 = b1/b9
			b9 = b1*x
			b9 = 3/b9
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