import numpy as np 

def function(x):

	p1 = x
	p7 = x
	paths = []
	try:
		if p1 <= 7:
			p7 = 2-p7
			x = 2-x
			p7 = p1-4
			paths.append(1)
		else:
			p1 = p1-6
			paths.append(2)
		if p7 <= 2:
			x = 7+x
			p1 = p1/p7
			paths.append(3)
		else:
			x = x/6
			p7 = 3+4
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