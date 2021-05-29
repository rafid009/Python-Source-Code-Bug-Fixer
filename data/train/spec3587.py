import numpy as np 

def function(x):

	b8 = x
	f3 = x
	paths = []
	try:
		if f3 <= 4:
			x = 9-5
			b8 = b8/f3
			paths.append(1)
		else:
			b8 = 0+9
			b8 = b8+5
			paths.append(2)
		if b8 > 7:
			f3 = x-6
			x = x/f3
			paths.append(3)
		else:
			x = b8+x
			f3 = 9+f3
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