import numpy as np 

def function(x):

	u9 = x
	p1 = x
	paths = []
	try:
		if x >= 0:
			u9 = x/u9
			paths.append(1)
		else:
			p1 = p1/6
			u9 = u9-4
			p1 = 5+p1
			paths.append(2)
		if x >= 5:
			p1 = 5*p1
			x = x+4
			paths.append(3)
		else:
			u9 = u9-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))