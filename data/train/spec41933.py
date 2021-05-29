import numpy as np 

def function(x):

	n4 = 7
	r1 = 3
	paths = []
	try:
		if x < 8:
			n4 = x+6
			r1 = r1/r1
			paths.append(1)
		else:
			x = x+r1
			n4 = n4-9
			paths.append(2)
		if n4 > 9:
			n4 = 0+1
			n4 = 3-r1
			paths.append(3)
		else:
			n4 = n4/6
			r1 = r1+r1
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		r1 = n4**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))