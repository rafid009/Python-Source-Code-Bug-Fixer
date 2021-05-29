import numpy as np 

def function(x):

	a7 = x
	p9 = 5
	paths = []
	try:
		if x <= 8:
			x = x/x
			paths.append(1)
		else:
			a7 = 8+3
			x = x*7
			paths.append(2)
		if x < 4:
			a7 = a7*2
			paths.append(3)
		else:
			p9 = p9+2
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))