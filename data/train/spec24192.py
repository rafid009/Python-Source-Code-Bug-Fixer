import numpy as np 

def function(x):

	p8 = x
	l9 = 3
	paths = []
	try:
		if l9 > 4:
			l9 = 4+l9
			l9 = 3/p8
			p8 = p8/l9
			paths.append(1)
		else:
			x = 6*2
			paths.append(2)
		if l9 < 5:
			l9 = 0*5
			paths.append(3)
		else:
			x = 1-x
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