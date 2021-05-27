import numpy as np 

def function(x):

	p8 = 2
	j0 = x
	x = 0
	paths = []
	try:
		if p8 <= 0:
			x = x+7
			p8 = p8*8
			paths.append(1)
		else:
			j0 = j0+1
			p8 = p8+7
			paths.append(2)
		if x < 6:
			x = x+6
			p8 = 5-p8
			x = x+0
			paths.append(3)
		else:
			p8 = x-3
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