import numpy as np 

def function(x):

	b5 = 7
	u5 = 8
	paths = []
	try:
		if b5 > 5:
			x = u5*x
			b5 = b5-6
			x = x+x
			paths.append(1)
		else:
			b5 = 8-x
			b5 = b5/b5
			x = 9*x
			paths.append(2)
		if u5 >= 0:
			x = 2-5
			paths.append(3)
		else:
			b5 = 7*u5
			u5 = u5/u5
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