import numpy as np 

def function(x):

	p8 = 3
	n7 = x
	x = 4
	paths = []
	try:
		if n7 < 3:
			x = p8*x
			x = x*4
			paths.append(1)
		else:
			p8 = 8/n7
			x = x+9
			paths.append(2)
		if p8 <= 1:
			p8 = p8+6
			p8 = p8/p8
			x = x+5
			paths.append(3)
		else:
			p8 = 0-p8
			n7 = x/n7
			n7 = n7/2
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))