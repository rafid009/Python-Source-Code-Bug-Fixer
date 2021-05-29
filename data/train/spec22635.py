import numpy as np 

def function(x):

	k2 = x
	p8 = 5
	paths = []
	try:
		if p8 < 6:
			p8 = k2+6
			p8 = 7*5
			x = x*9
			paths.append(1)
		else:
			k2 = x/k2
			k2 = k2+x
			paths.append(2)
		if p8 < 2:
			p8 = 9/p8
			x = 2+x
			x = x*x
			paths.append(3)
		else:
			p8 = 9*x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		k2 = p8**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))