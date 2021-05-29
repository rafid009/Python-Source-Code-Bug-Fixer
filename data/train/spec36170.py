import numpy as np 

def function(x):

	b4 = x
	f7 = 6
	paths = []
	try:
		if f7 <= 8:
			x = x/f7
			paths.append(1)
		else:
			x = x+9
			x = x-4
			b4 = 8*9
			paths.append(2)
		if b4 < 4:
			f7 = 6/f7
			paths.append(3)
		else:
			x = 9+7
			b4 = 3*b4
			f7 = f7+9
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