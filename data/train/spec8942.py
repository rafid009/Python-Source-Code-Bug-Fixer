import numpy as np 

def function(x):

	b3 = x
	b1 = x
	paths = []
	try:
		if b3 >= 7:
			x = 1-x
			paths.append(1)
		else:
			b1 = 5-b1
			b3 = 3-b3
			b1 = b1+1
			paths.append(2)
		if b1 <= 8:
			x = 2-b3
			x = b3+x
			b3 = b3+b3
			paths.append(3)
		else:
			x = x*4
			b1 = 0-1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))