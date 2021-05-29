import numpy as np 

def function(x):

	b0 = x
	f7 = 6
	paths = []
	try:
		if b0 <= 1:
			f7 = 1-f7
			paths.append(1)
		else:
			x = x*1
			x = 0/9
			paths.append(2)
		if b0 > 6:
			f7 = f7+9
			b0 = 1-6
			paths.append(3)
		else:
			b0 = 3/b0
			x = f7+f7
			x = x-4
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