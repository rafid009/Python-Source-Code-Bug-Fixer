import numpy as np 

def function(x):

	e0 = x
	p2 = 0
	paths = []
	try:
		if p2 <= 9:
			x = x+p2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if p2 > 3:
			p2 = 9-p2
			paths.append(3)
		else:
			e0 = e0+7
			x = x/4
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))