import numpy as np 

def function(x):

	u2 = x
	p2 = 4
	paths = []
	try:
		if u2 < 0:
			p2 = 9-2
			p2 = 8/u2
			x = x/3
			paths.append(1)
		else:
			u2 = u2*5
			paths.append(2)
		if x >= 5:
			x = 1+4
			u2 = u2*3
			paths.append(3)
		else:
			u2 = 4+1
			u2 = u2/9
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))