import numpy as np 

def function(x):

	b7 = 5
	l0 = x
	paths = []
	try:
		if b7 >= 3:
			l0 = l0/1
			x = l0/5
			paths.append(1)
		else:
			x = 3+b7
			x = 9/x
			paths.append(2)
		if x <= 4:
			b7 = 8/x
			x = x-x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))