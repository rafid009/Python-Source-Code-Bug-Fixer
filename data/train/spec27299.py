import numpy as np 

def function(x):

	p2 = x
	v9 = x
	paths = []
	try:
		if p2 < 2:
			p2 = 7/p2
			x = 4/x
			p2 = p2/1
			paths.append(1)
		else:
			v9 = 3+4
			x = 7/x
			paths.append(2)
		if x < 5:
			x = v9-2
			paths.append(3)
		else:
			v9 = 8*8
			x = x+3
			x = 1/5
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))