import numpy as np 

def function(x):

	f8 = 1
	b0 = 1
	paths = []
	try:
		if f8 <= 5:
			f8 = 1+f8
			b0 = 5-b0
			b0 = x+5
			paths.append(1)
		else:
			b0 = f8-f8
			b0 = x/b0
			paths.append(2)
		if b0 < 6:
			b0 = b0+5
			f8 = f8/3
			f8 = 9-b0
			paths.append(3)
		else:
			b0 = 3-b0
			b0 = 7/b0
			b0 = f8/b0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))