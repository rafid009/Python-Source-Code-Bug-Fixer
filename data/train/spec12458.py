import numpy as np 

def function(x):

	u4 = x
	p8 = 5
	x = x
	paths = []
	try:
		if p8 > 6:
			x = 8*p8
			paths.append(1)
		else:
			p8 = p8-x
			x = x/7
			paths.append(2)
		if u4 <= 6:
			x = 5-2
			paths.append(3)
		else:
			x = x+5
			x = u4+3
			x = p8/x
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