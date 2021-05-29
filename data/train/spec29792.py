import numpy as np 

def function(x):

	p8 = x
	n7 = 0
	paths = []
	try:
		if n7 < 7:
			p8 = 7/p8
			p8 = p8/1
			paths.append(1)
		else:
			p8 = 4*p8
			n7 = 8/n7
			n7 = n7+n7
			paths.append(2)
		if x >= 7:
			p8 = 6-9
			x = x+x
			p8 = p8/9
			paths.append(3)
		else:
			n7 = 4+3
			x = 8+n7
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