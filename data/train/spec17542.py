import numpy as np 

def function(x):

	p4 = x
	e9 = 1
	paths = []
	try:
		if x <= 6:
			e9 = e9-7
			p4 = p4+1
			paths.append(1)
		else:
			e9 = e9-9
			p4 = 5*5
			p4 = p4/6
			paths.append(2)
		if x <= 6:
			e9 = e9+9
			paths.append(3)
		else:
			x = 3*4
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