import numpy as np 

def function(x):

	p9 = 2
	u2 = x
	paths = []
	try:
		if u2 < 7:
			x = x/p9
			paths.append(1)
		else:
			p9 = 5/9
			u2 = 1-u2
			paths.append(2)
		if x < 2:
			p9 = x-p9
			paths.append(3)
		else:
			x = 8-u2
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