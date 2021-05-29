import numpy as np 

def function(x):

	q3 = 9
	p8 = x
	paths = []
	try:
		if q3 <= 0:
			p8 = p8+8
			x = x*4
			p8 = 4+p8
			paths.append(1)
		else:
			x = 4-x
			x = 8/x
			q3 = x-8
			paths.append(2)
		if x < 2:
			p8 = 3-p8
			p8 = p8-9
			paths.append(3)
		else:
			x = x*4
			q3 = q3+3
			x = x*7
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		p8 = q3**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))