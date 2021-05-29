import numpy as np 

def function(x):

	x2 = x
	p9 = x
	x = x
	paths = []
	try:
		if x > 2:
			p9 = p9-7
			paths.append(1)
		else:
			x2 = 1-p9
			paths.append(2)
		if p9 > 9:
			x = x+5
			p9 = p9+4
			x2 = p9+0
			paths.append(3)
		else:
			x = x/7
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