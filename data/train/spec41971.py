import numpy as np 

def function(x):

	b1 = 1
	n5 = 7
	paths = []
	try:
		if n5 <= 7:
			n5 = 0/5
			b1 = 0/b1
			paths.append(1)
		else:
			n5 = b1*n5
			paths.append(2)
		if n5 < 8:
			n5 = n5+2
			b1 = x+b1
			paths.append(3)
		else:
			b1 = b1+6
			n5 = n5-n5
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))