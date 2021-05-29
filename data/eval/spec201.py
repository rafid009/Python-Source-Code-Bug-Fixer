import numpy as np 

def function(x):

	p6 = x
	a1 = 7
	paths = []
	try:
		if p6 <= 5:
			x = x*8
			a1 = x*p6
			paths.append(1)
		else:
			a1 = 8+x
			p6 = 5-p6
			paths.append(2)
		if a1 > 8:
			p6 = 4/p6
			paths.append(3)
		else:
			a1 = 6/6
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))