import numpy as np 

def function(x):

	a5 = 8
	b3 = x
	x = 6
	paths = []
	try:
		if x > 9:
			b3 = a5+0
			x = x/2
			paths.append(1)
		else:
			x = b3*x
			paths.append(2)
		if a5 > 9:
			x = x-x
			paths.append(3)
		else:
			b3 = b3+4
			a5 = 5-5
			a5 = 7*a5
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))