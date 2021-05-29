import numpy as np 

def function(x):

	x9 = 8
	p1 = 5
	paths = []
	try:
		if x >= 3:
			p1 = x+p1
			x = 3/x
			paths.append(1)
		else:
			p1 = 2-p1
			p1 = p1/6
			paths.append(2)
		if p1 >= 0:
			x9 = p1*8
			p1 = p1-9
			paths.append(3)
		else:
			x9 = x9/x
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