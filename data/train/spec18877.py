import numpy as np 

def function(x):

	p2 = 4
	f0 = 1
	paths = []
	try:
		if x <= 5:
			p2 = p2-f0
			paths.append(1)
		else:
			p2 = p2*p2
			paths.append(2)
		if p2 >= 2:
			p2 = x/p2
			f0 = f0-8
			p2 = f0+p2
			paths.append(3)
		else:
			x = x/8
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