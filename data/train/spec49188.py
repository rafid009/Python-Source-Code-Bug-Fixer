import numpy as np 

def function(x):

	b5 = x
	n0 = 8
	x = 3
	paths = []
	try:
		if b5 <= 0:
			n0 = n0/7
			paths.append(1)
		else:
			x = b5+x
			n0 = n0-b5
			paths.append(2)
		if b5 <= 2:
			n0 = n0+1
			n0 = n0*0
			n0 = 3/1
			paths.append(3)
		else:
			x = 1+8
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		n0 = b5**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))