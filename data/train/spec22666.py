import numpy as np 

def function(x):

	q8 = 6
	p9 = x
	paths = []
	try:
		if x <= 9:
			x = 5-p9
			x = 0/x
			paths.append(1)
		else:
			p9 = 0/4
			paths.append(2)
		if p9 < 9:
			p9 = p9-6
			p9 = p9/6
			x = x-5
			paths.append(3)
		else:
			q8 = q8*p9
			x = p9+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))