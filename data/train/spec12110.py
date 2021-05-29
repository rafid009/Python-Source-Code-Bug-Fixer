import numpy as np 

def function(x):

	b1 = 0
	w3 = 4
	paths = []
	try:
		if b1 > 9:
			x = x/x
			paths.append(1)
		else:
			b1 = 0-x
			x = 5*x
			x = 6/x
			paths.append(2)
		if x <= 2:
			x = 0*7
			paths.append(3)
		else:
			x = 1/9
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))