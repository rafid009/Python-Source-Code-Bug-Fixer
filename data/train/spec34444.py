import numpy as np 

def function(x):

	p9 = x
	a5 = x
	x = 2
	paths = []
	try:
		if a5 <= 1:
			p9 = p9+p9
			paths.append(1)
		else:
			p9 = p9*3
			x = x+p9
			paths.append(2)
		if x > 9:
			a5 = a5-1
			a5 = a5+a5
			paths.append(3)
		else:
			p9 = 8-p9
			p9 = p9*5
			p9 = 0-p9
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))