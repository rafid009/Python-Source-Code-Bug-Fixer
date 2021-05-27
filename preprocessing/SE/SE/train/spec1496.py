import numpy as np 

def function(x):

	f5 = x
	b3 = x
	paths = []
	try:
		if x > 1:
			b3 = b3-4
			b3 = 7-5
			paths.append(1)
		else:
			f5 = f5*4
			b3 = b3-4
			paths.append(2)
		if x > 5:
			b3 = 6/b3
			f5 = 6*8
			paths.append(3)
		else:
			x = b3/3
			b3 = 6-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))