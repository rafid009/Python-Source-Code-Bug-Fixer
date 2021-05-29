import numpy as np 

def function(x):

	p8 = x
	v9 = x
	paths = []
	try:
		if x < 3:
			p8 = 9-0
			v9 = 6/v9
			paths.append(1)
		else:
			x = x*5
			x = 8-4
			x = 6/x
			paths.append(2)
		if p8 < 1:
			p8 = 2+2
			paths.append(3)
		else:
			p8 = 8-p8
			v9 = v9*v9
			v9 = v9*2
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))