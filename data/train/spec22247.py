import numpy as np 

def function(x):

	p8 = 4
	v7 = x
	paths = []
	try:
		if v7 >= 0:
			x = 6+9
			p8 = 8/p8
			v7 = 7/p8
			paths.append(1)
		else:
			p8 = p8/3
			p8 = 5+6
			v7 = x+p8
			paths.append(2)
		if v7 > 8:
			x = p8+x
			v7 = v7*9
			paths.append(3)
		else:
			p8 = 0-p8
			x = v7-0
			p8 = p8+2
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		p8 = v7**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))