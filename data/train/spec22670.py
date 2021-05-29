import numpy as np 

def function(x):

	v6 = 6
	p8 = 0
	paths = []
	try:
		if x >= 0:
			x = 6-7
			p8 = p8-p8
			paths.append(1)
		else:
			p8 = v6*5
			x = 9-v6
			paths.append(2)
		if x >= 6:
			x = x/1
			x = 2-x
			paths.append(3)
		else:
			v6 = 7+v6
			v6 = v6-8
			p8 = v6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))