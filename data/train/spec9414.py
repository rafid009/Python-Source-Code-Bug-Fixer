import numpy as np 

def function(x):

	v3 = x
	p8 = x
	x = 8
	paths = []
	try:
		if v3 > 4:
			x = 3/x
			paths.append(1)
		else:
			x = p8/6
			v3 = v3-0
			v3 = 2+v3
			paths.append(2)
		if x < 1:
			p8 = p8/v3
			paths.append(3)
		else:
			x = x-3
			v3 = 4*x
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))