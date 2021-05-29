import numpy as np 

def function(x):

	y2 = x
	p8 = x
	x = 7
	paths = []
	try:
		if p8 < 5:
			y2 = 4-y2
			x = 5*p8
			paths.append(1)
		else:
			y2 = x/2
			p8 = 4-p8
			x = x*x
			paths.append(2)
		if x > 7:
			p8 = 9*x
			paths.append(3)
		else:
			x = 6-7
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))