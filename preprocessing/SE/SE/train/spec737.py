import numpy as np 

def function(x):

	n2 = x
	r9 = x
	paths = []
	try:
		if x <= 3:
			x = x+x
			r9 = n2-r9
			paths.append(1)
		else:
			x = r9/x
			n2 = r9*r9
			x = x+n2
			paths.append(2)
		if x >= 1:
			n2 = n2+4
			x = r9/x
			x = 4-6
			paths.append(3)
		else:
			r9 = 2-7
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))