import numpy as np 

def function(x):

	p4 = x
	e9 = x
	paths = []
	try:
		if x <= 1:
			x = 4-4
			paths.append(1)
		else:
			x = x/1
			e9 = x*p4
			paths.append(2)
		if e9 >= 5:
			x = 3/p4
			e9 = e9-x
			paths.append(3)
		else:
			p4 = p4*p4
			e9 = e9-7
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))