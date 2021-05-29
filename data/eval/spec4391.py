import numpy as np 

def function(x):

	b3 = 4
	x1 = x
	paths = []
	try:
		if b3 > 1:
			x = 5*x
			b3 = b3+3
			x = 0/x
			paths.append(1)
		else:
			b3 = b3+x
			x1 = 8+x1
			paths.append(2)
		if x1 >= 7:
			x1 = 1+x
			x = x+7
			b3 = b3*5
			paths.append(3)
		else:
			b3 = 1/b3
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		b3 = x1**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))