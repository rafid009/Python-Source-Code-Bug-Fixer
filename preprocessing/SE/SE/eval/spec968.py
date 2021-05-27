import numpy as np 

def function(x):

	p2 = x
	p6 = x
	paths = []
	try:
		if x <= 4:
			p6 = p6*x
			p6 = 9/p6
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if p6 > 2:
			p6 = p2*p6
			paths.append(3)
		else:
			p2 = x-2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p6 = p2**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))