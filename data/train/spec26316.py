import numpy as np 

def function(x):

	p9 = 7
	paths = []
	try:
		if p9 > 2:
			p9 = p9-8
			paths.append(1)
		else:
			p9 = p9+3
			p9 = p9*5
			x = x+9
			paths.append(2)
		if x >= 0:
			p9 = p9-3
			p9 = 3-p9
			x = 5+8
			paths.append(3)
		else:
			x = x/2
			p9 = p9-7
			x = p9*8
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))