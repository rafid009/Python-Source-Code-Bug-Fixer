import numpy as np 

def function(x):

	l2 = x
	b3 = 1
	paths = []
	try:
		if x < 4:
			b3 = 5+b3
			b3 = 7/2
			paths.append(1)
		else:
			l2 = l2-4
			x = x+5
			l2 = 0*6
			paths.append(2)
		if l2 >= 2:
			b3 = b3*9
			paths.append(3)
		else:
			b3 = b3-6
			l2 = 5-5
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))