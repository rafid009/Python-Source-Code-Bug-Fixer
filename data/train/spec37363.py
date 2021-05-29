import numpy as np 

def function(x):

	u4 = 2
	p0 = 9
	paths = []
	try:
		if u4 <= 2:
			p0 = p0-1
			u4 = x-u4
			u4 = 1-u4
			paths.append(1)
		else:
			x = 5-6
			paths.append(2)
		if x >= 2:
			x = x-1
			p0 = 2/p0
			paths.append(3)
		else:
			x = 2-4
			p0 = 7-p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))