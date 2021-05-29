import numpy as np 

def function(x):

	o1 = x
	b5 = 5
	paths = []
	try:
		if x < 3:
			b5 = 0/b5
			b5 = 8*b5
			b5 = 9*b5
			paths.append(1)
		else:
			o1 = o1*9
			paths.append(2)
		if b5 <= 5:
			x = 6/x
			b5 = b5+b5
			x = x-5
			paths.append(3)
		else:
			b5 = b5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))