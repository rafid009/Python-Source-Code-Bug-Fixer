import numpy as np 

def function(x):

	p8 = x
	k2 = 2
	paths = []
	try:
		if k2 < 8:
			k2 = 5*k2
			x = x+0
			k2 = k2+7
			paths.append(1)
		else:
			p8 = x/p8
			p8 = 7/x
			paths.append(2)
		if p8 <= 3:
			p8 = p8+p8
			p8 = p8/8
			x = p8/3
			paths.append(3)
		else:
			p8 = p8-2
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))