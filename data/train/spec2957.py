import numpy as np 

def function(x):

	p2 = 8
	e9 = x
	paths = []
	try:
		if x < 7:
			x = x+2
			paths.append(1)
		else:
			e9 = e9*p2
			p2 = e9*p2
			paths.append(2)
		if e9 > 6:
			p2 = p2/4
			p2 = p2-9
			paths.append(3)
		else:
			e9 = 3+e9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))