import numpy as np 

def function(x):

	l6 = 0
	p8 = 0
	paths = []
	try:
		if p8 <= 8:
			l6 = l6-5
			paths.append(1)
		else:
			p8 = 6+p8
			paths.append(2)
		if x <= 0:
			p8 = p8*7
			paths.append(3)
		else:
			p8 = l6*x
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