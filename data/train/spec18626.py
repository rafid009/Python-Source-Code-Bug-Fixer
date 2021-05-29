import numpy as np 

def function(x):

	p7 = x
	e5 = 7
	x = x
	paths = []
	try:
		if e5 > 8:
			e5 = 9*0
			paths.append(1)
		else:
			p7 = 9+1
			e5 = 5-x
			paths.append(2)
		if p7 > 8:
			p7 = p7-e5
			paths.append(3)
		else:
			e5 = e5+e5
			x = 3/p7
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))