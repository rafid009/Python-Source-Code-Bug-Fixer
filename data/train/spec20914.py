import numpy as np 

def function(x):

	p9 = 8
	p6 = x
	paths = []
	try:
		if x < 6:
			x = x*9
			x = x*2
			x = 0-x
			paths.append(1)
		else:
			x = x/p9
			p9 = p9+2
			p9 = 3-1
			paths.append(2)
		if x >= 3:
			x = 9*x
			x = 9*p6
			paths.append(3)
		else:
			p9 = p9+p6
			p9 = p6*5
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p9 = p6**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))