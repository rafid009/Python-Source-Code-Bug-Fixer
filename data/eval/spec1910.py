import numpy as np 

def function(x):

	a5 = x
	p8 = x
	paths = []
	try:
		if p8 <= 9:
			x = p8-x
			p8 = 8+p8
			a5 = a5-4
			paths.append(1)
		else:
			x = 3*6
			paths.append(2)
		if a5 > 6:
			a5 = a5-5
			a5 = p8*a5
			p8 = p8/p8
			paths.append(3)
		else:
			a5 = 5+a5
			p8 = 5/p8
			x = p8+1
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		p8 = a5**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))