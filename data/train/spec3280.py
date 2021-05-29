import numpy as np 

def function(x):

	r6 = 7
	n4 = x
	paths = []
	try:
		if n4 < 8:
			n4 = 5*n4
			paths.append(1)
		else:
			x = 6-x
			r6 = r6+5
			x = 9/8
			paths.append(2)
		if r6 <= 0:
			x = 4+5
			x = 4*3
			paths.append(3)
		else:
			n4 = n4+3
			r6 = 4*5
			n4 = 3+x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		r6 = n4**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))