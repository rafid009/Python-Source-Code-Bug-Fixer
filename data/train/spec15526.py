import numpy as np 

def function(x):

	n7 = 0
	b7 = 2
	x = 8
	paths = []
	try:
		if n7 <= 5:
			b7 = 9/b7
			paths.append(1)
		else:
			n7 = 9/3
			b7 = b7+b7
			paths.append(2)
		if b7 < 4:
			x = x+x
			paths.append(3)
		else:
			x = 1*n7
			x = 5+x
			n7 = 1-b7
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))