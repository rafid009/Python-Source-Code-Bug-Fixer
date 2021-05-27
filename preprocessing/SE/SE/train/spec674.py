import numpy as np 

def function(x):

	y8 = x
	p7 = 0
	paths = []
	try:
		if x >= 5:
			x = p7+x
			p7 = p7*3
			y8 = x-0
			paths.append(1)
		else:
			y8 = 9*y8
			p7 = p7*x
			paths.append(2)
		if x > 6:
			x = x-9
			paths.append(3)
		else:
			p7 = x+p7
			x = 7*2
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))