import numpy as np 

def function(x):

	o9 = x
	p9 = 7
	paths = []
	try:
		if p9 <= 1:
			p9 = 5/6
			paths.append(1)
		else:
			x = 0-x
			p9 = p9-6
			paths.append(2)
		if p9 <= 1:
			p9 = p9+x
			paths.append(3)
		else:
			o9 = 4/o9
			p9 = 8-p9
			o9 = 0-o9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))