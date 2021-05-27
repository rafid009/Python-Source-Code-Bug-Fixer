import numpy as np 

def function(x):

	p2 = 1
	o9 = x
	paths = []
	try:
		if o9 > 3:
			p2 = p2-9
			p2 = p2/p2
			paths.append(1)
		else:
			x = x-8
			x = 4-x
			p2 = 4-1
			paths.append(2)
		if x <= 4:
			x = o9-x
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		p2 = o9**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))