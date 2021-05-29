import numpy as np 

def function(x):

	n0 = x
	r9 = 9
	paths = []
	try:
		if x < 0:
			r9 = n0+r9
			r9 = r9-5
			paths.append(1)
		else:
			x = x+3
			x = 9*0
			x = x+6
			paths.append(2)
		if r9 > 3:
			n0 = r9*n0
			n0 = 5+n0
			paths.append(3)
		else:
			x = x*9
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