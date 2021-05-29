import numpy as np 

def function(x):

	n4 = x
	b9 = 3
	paths = []
	try:
		if n4 > 0:
			n4 = b9+x
			b9 = n4-8
			n4 = b9+b9
			paths.append(1)
		else:
			n4 = 7-n4
			x = x+0
			n4 = n4-n4
			paths.append(2)
		if b9 >= 3:
			b9 = 2*b9
			b9 = n4*b9
			paths.append(3)
		else:
			b9 = n4+b9
			b9 = n4-b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))