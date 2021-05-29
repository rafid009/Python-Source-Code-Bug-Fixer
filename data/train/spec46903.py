import numpy as np 

def function(x):

	b4 = 5
	b0 = 7
	x = x
	paths = []
	try:
		if b0 < 0:
			x = b0*9
			x = 2+x
			paths.append(1)
		else:
			b4 = b0/4
			b0 = b0-3
			b4 = b4-b0
			paths.append(2)
		if x > 9:
			b0 = 0+b0
			b4 = x+8
			paths.append(3)
		else:
			b0 = b0+b0
			b4 = 2/b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b0 = b4**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))