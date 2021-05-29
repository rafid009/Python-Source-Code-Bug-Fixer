import numpy as np 

def function(x):

	a7 = 0
	p6 = x
	x = 6
	paths = []
	try:
		if a7 > 9:
			x = 9-4
			x = 5-2
			x = 1*8
			paths.append(1)
		else:
			a7 = a7-3
			a7 = a7+9
			p6 = 6+p6
			paths.append(2)
		if x > 9:
			p6 = 1*4
			paths.append(3)
		else:
			a7 = p6/6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))