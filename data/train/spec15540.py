import numpy as np 

def function(x):

	b6 = 5
	x7 = 6
	paths = []
	try:
		if x7 < 8:
			x7 = 5-6
			b6 = b6/6
			paths.append(1)
		else:
			x7 = 5/x7
			paths.append(2)
		if x7 < 1:
			x = 1-x7
			b6 = b6+5
			b6 = 5-b6
			paths.append(3)
		else:
			x = x*2
			x = b6*x
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		b6 = x7**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))