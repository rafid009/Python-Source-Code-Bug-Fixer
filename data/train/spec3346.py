import numpy as np 

def function(x):

	p8 = 3
	p2 = 4
	paths = []
	try:
		if x <= 8:
			p8 = 3/p8
			x = p8*p8
			paths.append(1)
		else:
			x = 2+x
			p8 = p8/4
			paths.append(2)
		if p2 > 0:
			p2 = 0+p2
			p8 = p8-p2
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p2 = p8**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))