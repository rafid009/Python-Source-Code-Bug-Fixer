import numpy as np 

def function(x):

	v9 = 1
	p3 = x
	paths = []
	try:
		if p3 >= 8:
			p3 = 0+p3
			x = 4-4
			paths.append(1)
		else:
			p3 = 4+x
			p3 = p3*v9
			paths.append(2)
		if x < 0:
			x = v9/2
			v9 = v9+p3
			paths.append(3)
		else:
			p3 = 2/p3
			p3 = p3-3
			v9 = 7/v9
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		v9 = p3**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))