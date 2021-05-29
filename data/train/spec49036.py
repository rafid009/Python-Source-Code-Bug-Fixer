import numpy as np 

def function(x):

	n1 = x
	b5 = 8
	paths = []
	try:
		if n1 >= 2:
			n1 = b5-n1
			paths.append(1)
		else:
			b5 = b5+1
			n1 = 4*2
			b5 = 8/x
			paths.append(2)
		if n1 > 6:
			n1 = n1-b5
			x = x*4
			x = n1*8
			paths.append(3)
		else:
			x = x/b5
			b5 = b5+n1
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))