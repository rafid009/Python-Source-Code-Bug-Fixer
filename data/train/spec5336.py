import numpy as np 

def function(x):

	b1 = x
	n5 = x
	x = x
	paths = []
	try:
		if x <= 3:
			n5 = 3/n5
			b1 = b1+b1
			paths.append(1)
		else:
			n5 = 7+3
			b1 = 0/b1
			paths.append(2)
		if b1 > 1:
			b1 = 6-b1
			b1 = 2*b1
			b1 = 5-b1
			paths.append(3)
		else:
			n5 = 9/n5
			x = n5+4
			b1 = b1+1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))