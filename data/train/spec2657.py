import numpy as np 

def function(x):

	b0 = x
	b7 = x
	paths = []
	try:
		if b0 < 2:
			b7 = b7+7
			x = 1+7
			paths.append(1)
		else:
			b7 = x+b0
			paths.append(2)
		if x < 1:
			x = x*2
			paths.append(3)
		else:
			b7 = b7-3
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b7 = b0**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))