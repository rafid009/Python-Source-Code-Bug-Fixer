import numpy as np 

def function(x):

	e6 = x
	p2 = x
	paths = []
	try:
		if p2 > 5:
			e6 = 5-x
			p2 = p2*1
			paths.append(1)
		else:
			x = 6*1
			p2 = 1/e6
			paths.append(2)
		if x < 2:
			e6 = p2+9
			p2 = e6/x
			x = p2*x
			paths.append(3)
		else:
			x = 0+p2
			p2 = p2/e6
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))