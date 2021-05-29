import numpy as np 

def function(x):

	p9 = 8
	e0 = x
	paths = []
	try:
		if p9 <= 8:
			e0 = 6*e0
			x = x+6
			x = 0/x
			paths.append(1)
		else:
			x = 0+3
			x = x/e0
			paths.append(2)
		if e0 < 1:
			e0 = e0*3
			p9 = 7*x
			p9 = 9+e0
			paths.append(3)
		else:
			e0 = 1/p9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		e0 = p9**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))