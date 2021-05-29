import numpy as np 

def function(x):

	x2 = x
	p1 = 8
	x = 4
	paths = []
	try:
		if x2 > 8:
			p1 = x2/p1
			x = 4-x
			p1 = x/p1
			paths.append(1)
		else:
			p1 = 0-4
			paths.append(2)
		if x > 7:
			x2 = 3-x2
			paths.append(3)
		else:
			x = x+x2
			p1 = p1*4
			x2 = p1+0
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))