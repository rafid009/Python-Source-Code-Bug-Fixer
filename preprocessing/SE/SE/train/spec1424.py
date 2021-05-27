import numpy as np 

def function(x):

	p8 = x
	t8 = 1
	x = x
	paths = []
	try:
		if t8 < 4:
			p8 = 4+3
			p8 = 9*x
			paths.append(1)
		else:
			t8 = 2*3
			p8 = 8/p8
			x = 1*x
			paths.append(2)
		if p8 >= 4:
			t8 = t8+2
			paths.append(3)
		else:
			x = x-3
			x = x+4
			x = 6*8
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