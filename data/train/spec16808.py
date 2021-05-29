import numpy as np 

def function(x):

	b3 = x
	n2 = x
	paths = []
	try:
		if n2 >= 9:
			n2 = n2-b3
			paths.append(1)
		else:
			x = x*5
			b3 = x*b3
			x = 8/b3
			paths.append(2)
		if b3 < 6:
			b3 = b3+3
			paths.append(3)
		else:
			x = 3+4
			b3 = n2-b3
			x = x*b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		n2 = b3**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))