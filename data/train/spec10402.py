import numpy as np 

def function(x):

	y7 = x
	p2 = x
	paths = []
	try:
		if y7 <= 2:
			x = 8/x
			paths.append(1)
		else:
			y7 = 5-4
			paths.append(2)
		if x < 4:
			x = y7*x
			paths.append(3)
		else:
			p2 = p2+7
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))