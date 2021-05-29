import numpy as np 

def function(x):

	b6 = x
	f9 = x
	paths = []
	try:
		if b6 > 2:
			b6 = 8*7
			x = 0-b6
			x = x/5
			paths.append(1)
		else:
			f9 = x/f9
			b6 = 4+7
			paths.append(2)
		if x > 4:
			b6 = b6-x
			f9 = f9-b6
			paths.append(3)
		else:
			x = x-5
			b6 = 2+x
			x = 1*x
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