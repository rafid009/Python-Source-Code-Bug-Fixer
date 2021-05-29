import numpy as np 

def function(x):

	j6 = 2
	p8 = x
	paths = []
	try:
		if x < 0:
			x = x+6
			paths.append(1)
		else:
			x = 6+j6
			p8 = p8-x
			paths.append(2)
		if j6 > 7:
			p8 = 5+3
			x = j6-4
			x = p8*p8
			paths.append(3)
		else:
			j6 = 3-j6
			p8 = 2-p8
			p8 = p8-x
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