import numpy as np 

def function(x):

	p6 = 2
	f6 = x
	paths = []
	try:
		if p6 < 8:
			p6 = p6-x
			paths.append(1)
		else:
			x = x+p6
			paths.append(2)
		if p6 < 0:
			f6 = 9*3
			p6 = f6/p6
			f6 = p6-9
			paths.append(3)
		else:
			p6 = p6-3
			x = x+8
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))