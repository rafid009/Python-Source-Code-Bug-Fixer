import numpy as np 

def function(x):

	x5 = 8
	p8 = 7
	paths = []
	try:
		if x5 <= 2:
			x5 = x5-x5
			p8 = p8+x5
			p8 = 5+x
			paths.append(1)
		else:
			p8 = x5*8
			p8 = p8*x5
			paths.append(2)
		if p8 <= 7:
			x5 = p8+4
			p8 = p8*8
			p8 = p8+9
			paths.append(3)
		else:
			x = 3*x
			p8 = 5-8
			x = x+x5
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