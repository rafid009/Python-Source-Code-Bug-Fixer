import numpy as np 

def function(x):

	n0 = x
	b4 = x
	paths = []
	try:
		if b4 <= 5:
			n0 = 0-n0
			b4 = 5*n0
			paths.append(1)
		else:
			x = 0/6
			b4 = b4-2
			paths.append(2)
		if b4 >= 0:
			b4 = b4*3
			paths.append(3)
		else:
			b4 = 5+x
			b4 = b4*0
			b4 = x+x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))