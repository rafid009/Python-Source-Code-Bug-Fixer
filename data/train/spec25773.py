import numpy as np 

def function(x):

	a1 = 6
	b5 = x
	paths = []
	try:
		if a1 < 1:
			a1 = 3*a1
			b5 = b5+8
			x = x-3
			paths.append(1)
		else:
			x = 0/x
			x = 6/8
			paths.append(2)
		if a1 < 7:
			a1 = x/a1
			x = 0-x
			x = 3+x
			paths.append(3)
		else:
			x = a1+x
			a1 = 1/9
			a1 = a1/7
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))