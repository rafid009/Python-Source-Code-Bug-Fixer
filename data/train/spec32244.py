import numpy as np 

def function(x):

	p8 = 3
	j0 = x
	paths = []
	try:
		if j0 > 7:
			p8 = p8/x
			x = 0+x
			paths.append(1)
		else:
			p8 = p8*j0
			paths.append(2)
		if p8 >= 2:
			x = x-3
			p8 = 1/5
			paths.append(3)
		else:
			x = x+5
			j0 = 8-j0
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		j0 = p8**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))