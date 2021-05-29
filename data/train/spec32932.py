import numpy as np 

def function(x):

	f5 = 7
	b6 = x
	paths = []
	try:
		if f5 >= 7:
			b6 = x*3
			f5 = f5*8
			paths.append(1)
		else:
			b6 = b6-7
			b6 = b6-7
			x = b6-b6
			paths.append(2)
		if x >= 0:
			b6 = b6*3
			f5 = b6-x
			paths.append(3)
		else:
			b6 = b6-1
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