import numpy as np 

def function(x):

	b4 = 2
	x6 = x
	paths = []
	try:
		if x > 7:
			x6 = x-x6
			x6 = 7*0
			b4 = 9-b4
			paths.append(1)
		else:
			b4 = 4+b4
			x6 = 3/x6
			paths.append(2)
		if x < 6:
			b4 = x6*2
			paths.append(3)
		else:
			b4 = b4*6
			x = 6-x6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))