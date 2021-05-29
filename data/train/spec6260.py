import numpy as np 

def function(x):

	p9 = x
	h9 = x
	paths = []
	try:
		if x < 5:
			p9 = h9+p9
			x = 0+0
			p9 = p9*1
			paths.append(1)
		else:
			h9 = h9+0
			x = 5+x
			paths.append(2)
		if p9 >= 6:
			x = x/8
			h9 = h9-h9
			paths.append(3)
		else:
			p9 = h9/5
			x = 4-p9
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