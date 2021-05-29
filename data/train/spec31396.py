import numpy as np 

def function(x):

	i4 = 7
	b8 = 2
	paths = []
	try:
		if b8 <= 1:
			b8 = 2*7
			x = 1*x
			x = x-7
			paths.append(1)
		else:
			b8 = 6/i4
			paths.append(2)
		if i4 < 5:
			x = x+8
			b8 = b8+9
			x = x*1
			paths.append(3)
		else:
			b8 = b8/7
			b8 = b8-b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))