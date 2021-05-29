import numpy as np 

def function(x):

	h8 = 7
	p9 = x
	x = 5
	paths = []
	try:
		if x < 5:
			x = x/3
			paths.append(1)
		else:
			h8 = h8/4
			h8 = h8/5
			x = x/2
			paths.append(2)
		if h8 <= 5:
			x = x+9
			paths.append(3)
		else:
			p9 = p9-p9
			p9 = p9/p9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))