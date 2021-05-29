import numpy as np 

def function(x):

	q3 = x
	b1 = 6
	paths = []
	try:
		if b1 > 6:
			b1 = q3+8
			paths.append(1)
		else:
			b1 = b1+9
			paths.append(2)
		if x <= 8:
			b1 = b1+6
			x = x-8
			b1 = b1*7
			paths.append(3)
		else:
			b1 = b1*9
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))