import numpy as np 

def function(x):

	n0 = x
	p9 = 8
	paths = []
	try:
		if x < 5:
			x = x/9
			paths.append(1)
		else:
			n0 = n0+8
			paths.append(2)
		if p9 >= 2:
			n0 = n0+x
			x = n0*7
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		p9 = n0**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))