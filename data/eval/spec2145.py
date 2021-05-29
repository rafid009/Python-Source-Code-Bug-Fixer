import numpy as np 

def function(x):

	e4 = x
	b1 = 5
	paths = []
	try:
		if b1 > 8:
			e4 = e4/5
			paths.append(1)
		else:
			x = e4-5
			b1 = b1-6
			x = b1*1
			paths.append(2)
		if x > 2:
			x = x-1
			x = b1+b1
			paths.append(3)
		else:
			x = x*2
			b1 = 5+b1
			e4 = 5-e4
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