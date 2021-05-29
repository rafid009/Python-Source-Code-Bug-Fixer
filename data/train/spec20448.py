import numpy as np 

def function(x):

	n7 = x
	b9 = 5
	paths = []
	try:
		if b9 <= 0:
			n7 = 7/2
			paths.append(1)
		else:
			b9 = 0+3
			paths.append(2)
		if n7 <= 6:
			x = x+x
			b9 = 6*4
			paths.append(3)
		else:
			n7 = 7+n7
			n7 = b9-5
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