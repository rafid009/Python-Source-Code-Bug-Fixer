import numpy as np 

def function(x):

	b3 = 5
	f1 = 4
	paths = []
	try:
		if b3 >= 8:
			b3 = 6-7
			x = b3+b3
			f1 = f1/b3
			paths.append(1)
		else:
			b3 = f1+x
			b3 = b3+7
			paths.append(2)
		if f1 <= 1:
			x = x-2
			paths.append(3)
		else:
			b3 = 8*7
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