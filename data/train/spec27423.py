import numpy as np 

def function(x):

	b5 = 7
	n3 = x
	paths = []
	try:
		if b5 < 7:
			b5 = 5*b5
			n3 = n3*9
			b5 = b5-2
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if n3 > 8:
			x = b5-n3
			paths.append(3)
		else:
			b5 = 7-0
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))