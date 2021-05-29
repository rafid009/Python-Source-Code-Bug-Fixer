import numpy as np 

def function(x):

	p8 = x
	y9 = x
	paths = []
	try:
		if y9 >= 4:
			p8 = p8/1
			p8 = p8-0
			x = x+2
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if p8 < 2:
			x = x*7
			p8 = 0-x
			p8 = y9*1
			paths.append(3)
		else:
			x = y9-x
			p8 = p8-p8
			p8 = p8+5
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		y9 = p8**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))