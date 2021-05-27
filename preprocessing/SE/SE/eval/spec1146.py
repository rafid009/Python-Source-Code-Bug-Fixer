import numpy as np 

def function(x):

	f5 = x
	b6 = 7
	paths = []
	try:
		if b6 <= 7:
			f5 = f5+x
			b6 = 6/b6
			b6 = b6+8
			paths.append(1)
		else:
			f5 = 2+4
			b6 = 3/b6
			paths.append(2)
		if b6 < 4:
			b6 = b6*7
			x = x*4
			paths.append(3)
		else:
			b6 = 7+3
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