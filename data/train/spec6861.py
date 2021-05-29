import numpy as np 

def function(x):

	x1 = 5
	b3 = 5
	paths = []
	try:
		if x1 <= 1:
			x1 = 9*x1
			paths.append(1)
		else:
			x1 = x/b3
			x1 = x1-1
			paths.append(2)
		if b3 > 3:
			b3 = 4-6
			paths.append(3)
		else:
			b3 = 8+b3
			x = x-2
			x1 = x1*0
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