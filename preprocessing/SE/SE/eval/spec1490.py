import numpy as np 

def function(x):

	b4 = 7
	b0 = 4
	paths = []
	try:
		if b0 <= 5:
			b0 = b4/4
			x = x*7
			paths.append(1)
		else:
			x = b0+x
			b4 = b4-b0
			x = 9-6
			paths.append(2)
		if b4 < 4:
			b4 = 0-x
			paths.append(3)
		else:
			b4 = 7*b4
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))