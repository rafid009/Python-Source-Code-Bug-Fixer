import numpy as np 

def function(x):

	n4 = x
	r3 = 4
	x = x
	paths = []
	try:
		if r3 > 0:
			n4 = n4/r3
			x = x+x
			paths.append(1)
		else:
			n4 = n4+n4
			r3 = 1+r3
			paths.append(2)
		if n4 <= 6:
			x = 2/x
			x = 1+0
			paths.append(3)
		else:
			r3 = n4+5
			r3 = r3+x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))