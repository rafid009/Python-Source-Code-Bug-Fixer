import numpy as np 

def function(x):

	b9 = 3
	n7 = x
	paths = []
	try:
		if x >= 7:
			b9 = x*b9
			n7 = 9-8
			n7 = 2*n7
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if x > 5:
			x = x+8
			x = x+x
			paths.append(3)
		else:
			b9 = b9*b9
			b9 = b9/6
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		b9 = n7**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))