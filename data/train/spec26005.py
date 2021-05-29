import numpy as np 

def function(x):

	p8 = x
	o0 = 4
	paths = []
	try:
		if x >= 5:
			x = 0-7
			p8 = p8+5
			p8 = p8+8
			paths.append(1)
		else:
			p8 = p8+p8
			paths.append(2)
		if x < 1:
			x = p8*8
			p8 = x/o0
			paths.append(3)
		else:
			p8 = 5+p8
			o0 = p8-0
			x = 0-6
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