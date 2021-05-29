import numpy as np 

def function(x):

	b9 = 8
	a3 = x
	paths = []
	try:
		if x > 9:
			x = a3-9
			b9 = x*6
			paths.append(1)
		else:
			b9 = x+3
			b9 = b9+6
			a3 = a3/7
			paths.append(2)
		if b9 > 0:
			b9 = b9+2
			x = x-a3
			a3 = 3-a3
			paths.append(3)
		else:
			x = a3*b9
			b9 = x-4
			b9 = 6/b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))