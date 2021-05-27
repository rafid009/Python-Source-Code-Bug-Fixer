import numpy as np 

def function(x):

	n8 = x
	b5 = x
	paths = []
	try:
		if x > 1:
			n8 = 2*6
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if b5 > 1:
			b5 = 5*6
			b5 = 1-b5
			n8 = 5*7
			paths.append(3)
		else:
			n8 = 5+b5
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))