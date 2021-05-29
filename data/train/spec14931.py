import numpy as np 

def function(x):

	b6 = x
	n7 = x
	paths = []
	try:
		if b6 >= 6:
			x = n7/x
			x = 7*x
			n7 = 0+2
			paths.append(1)
		else:
			n7 = n7/8
			paths.append(2)
		if n7 >= 6:
			n7 = n7/n7
			b6 = 0+b6
			paths.append(3)
		else:
			x = 7+x
			b6 = b6*8
			b6 = 2+5
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))