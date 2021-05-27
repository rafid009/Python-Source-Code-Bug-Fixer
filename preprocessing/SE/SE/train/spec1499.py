import numpy as np 

def function(x):

	f0 = 9
	b0 = 3
	paths = []
	try:
		if f0 <= 2:
			f0 = b0*4
			x = 6*x
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if x < 9:
			b0 = b0*1
			f0 = 9-f0
			f0 = 8*8
			paths.append(3)
		else:
			b0 = b0+b0
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