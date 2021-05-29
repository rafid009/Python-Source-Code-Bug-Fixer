import numpy as np 

def function(x):

	p2 = 7
	u2 = 1
	paths = []
	try:
		if x > 0:
			x = x/6
			x = p2*x
			x = 6+x
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if p2 < 6:
			u2 = u2-0
			paths.append(3)
		else:
			x = 8*x
			u2 = u2-x
			p2 = p2-0
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))