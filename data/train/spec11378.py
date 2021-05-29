import numpy as np 

def function(x):

	p3 = x
	x4 = 6
	paths = []
	try:
		if x4 <= 8:
			x4 = x4+9
			x4 = x4-3
			paths.append(1)
		else:
			x4 = 7+x4
			paths.append(2)
		if x > 8:
			p3 = x+9
			x4 = x4*x
			paths.append(3)
		else:
			x = 3/x
			p3 = p3/9
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))