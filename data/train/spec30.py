import numpy as np 

def function(x):

	n3 = x
	b5 = 8
	paths = []
	try:
		if n3 <= 5:
			x = x/5
			paths.append(1)
		else:
			n3 = 1/n3
			paths.append(2)
		if b5 > 3:
			b5 = b5-4
			b5 = b5/n3
			paths.append(3)
		else:
			n3 = 4*x
			x = x+n3
			x = n3-x
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