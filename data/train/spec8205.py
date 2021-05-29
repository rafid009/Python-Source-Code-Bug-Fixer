import numpy as np 

def function(x):

	l6 = x
	p9 = 6
	paths = []
	try:
		if p9 <= 8:
			p9 = 3-p9
			paths.append(1)
		else:
			l6 = l6+8
			paths.append(2)
		if x >= 3:
			x = 8/l6
			paths.append(3)
		else:
			p9 = p9+p9
			x = 9-x
			p9 = p9-5
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