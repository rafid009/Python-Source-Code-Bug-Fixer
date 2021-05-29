import numpy as np 

def function(x):

	x9 = 5
	p1 = x
	x = 1
	paths = []
	try:
		if p1 < 0:
			x9 = x9/5
			x = x/4
			paths.append(1)
		else:
			p1 = 2+x9
			paths.append(2)
		if p1 > 7:
			x9 = x-x9
			paths.append(3)
		else:
			x9 = 3*5
			x9 = x9+2
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