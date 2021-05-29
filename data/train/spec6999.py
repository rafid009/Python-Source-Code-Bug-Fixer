import numpy as np 

def function(x):

	a8 = x
	p9 = x
	paths = []
	try:
		if p9 >= 1:
			a8 = a8-3
			x = 9+5
			paths.append(1)
		else:
			a8 = a8+9
			paths.append(2)
		if x < 3:
			x = p9/x
			a8 = 4*4
			x = 4+a8
			paths.append(3)
		else:
			a8 = 8*a8
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))