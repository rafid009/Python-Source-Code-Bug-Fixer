import numpy as np 

def function(x):

	u9 = x
	p0 = 2
	paths = []
	try:
		if p0 >= 8:
			u9 = 4*u9
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x > 2:
			x = 0-6
			paths.append(3)
		else:
			p0 = x/p0
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		p0 = u9**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))