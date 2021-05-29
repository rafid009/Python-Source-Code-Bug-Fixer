import numpy as np 

def function(x):

	b1 = x
	a5 = x
	paths = []
	try:
		if a5 >= 1:
			a5 = b1*8
			a5 = 9*a5
			b1 = 4/b1
			paths.append(1)
		else:
			a5 = a5*8
			b1 = b1-4
			a5 = a5+2
			paths.append(2)
		if b1 <= 0:
			x = 1+8
			x = 9/x
			paths.append(3)
		else:
			a5 = a5+6
			b1 = 6*6
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))