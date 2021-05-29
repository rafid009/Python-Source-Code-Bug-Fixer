import numpy as np 

def function(x):

	v0 = x
	p2 = x
	paths = []
	try:
		if x < 6:
			p2 = p2+7
			v0 = p2-9
			paths.append(1)
		else:
			v0 = 2-9
			paths.append(2)
		if x > 4:
			x = v0+x
			v0 = v0/7
			p2 = p2-5
			paths.append(3)
		else:
			p2 = 3/5
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