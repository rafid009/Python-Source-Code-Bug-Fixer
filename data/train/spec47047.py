import numpy as np 

def function(x):

	p9 = x
	o9 = 1
	paths = []
	try:
		if x <= 6:
			p9 = p9+3
			o9 = o9-3
			paths.append(1)
		else:
			p9 = o9+p9
			o9 = x-o9
			p9 = p9-3
			paths.append(2)
		if x >= 7:
			o9 = 7+o9
			p9 = o9+p9
			paths.append(3)
		else:
			x = 9*x
			p9 = o9/x
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		o9 = p9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))