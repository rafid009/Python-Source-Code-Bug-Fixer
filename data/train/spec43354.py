import numpy as np 

def function(x):

	a1 = x
	p9 = x
	paths = []
	try:
		if x >= 9:
			a1 = p9+a1
			p9 = 5*7
			paths.append(1)
		else:
			p9 = p9+6
			a1 = 5+a1
			x = x-6
			paths.append(2)
		if p9 <= 9:
			a1 = x+a1
			x = 6/x
			paths.append(3)
		else:
			x = a1+a1
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