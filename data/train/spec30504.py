import numpy as np 

def function(x):

	n6 = x
	b7 = 7
	paths = []
	try:
		if b7 >= 5:
			b7 = 5-1
			b7 = b7-b7
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if n6 >= 3:
			n6 = n6+5
			n6 = n6-x
			paths.append(3)
		else:
			b7 = b7-2
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		b7 = n6**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))