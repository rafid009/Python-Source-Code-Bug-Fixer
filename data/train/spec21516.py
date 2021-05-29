import numpy as np 

def function(x):

	p2 = x
	u6 = x
	paths = []
	try:
		if u6 <= 0:
			p2 = 4/p2
			x = x*6
			u6 = u6+0
			paths.append(1)
		else:
			p2 = p2/4
			u6 = p2+8
			x = x+u6
			paths.append(2)
		if x > 0:
			x = x-1
			u6 = u6+0
			paths.append(3)
		else:
			u6 = 1-u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))