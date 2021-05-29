import numpy as np 

def function(x):

	p8 = x
	n9 = 0
	x = 3
	paths = []
	try:
		if p8 >= 1:
			x = 7/x
			p8 = p8-p8
			paths.append(1)
		else:
			n9 = 7*8
			n9 = n9+1
			paths.append(2)
		if x <= 9:
			x = 4+2
			paths.append(3)
		else:
			n9 = n9*3
			p8 = 0+p8
			x = x/p8
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