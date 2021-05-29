import numpy as np 

def function(x):

	n9 = 7
	r3 = x
	paths = []
	try:
		if r3 < 0:
			n9 = n9/r3
			x = x/3
			paths.append(1)
		else:
			r3 = r3*n9
			r3 = 6-r3
			n9 = n9*6
			paths.append(2)
		if r3 > 1:
			r3 = 4+4
			r3 = r3-r3
			paths.append(3)
		else:
			r3 = 6+r3
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))