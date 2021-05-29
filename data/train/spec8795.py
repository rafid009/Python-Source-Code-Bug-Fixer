import numpy as np 

def function(x):

	x4 = x
	p4 = 8
	paths = []
	try:
		if p4 <= 8:
			x4 = 3+x4
			p4 = 7-p4
			x = x-x
			paths.append(1)
		else:
			p4 = 2*p4
			x = x+1
			paths.append(2)
		if x < 6:
			x4 = x4/9
			p4 = x-x4
			paths.append(3)
		else:
			p4 = p4+8
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))