import numpy as np 

def function(x):

	p8 = 3
	l2 = x
	paths = []
	try:
		if x < 4:
			l2 = l2/l2
			paths.append(1)
		else:
			l2 = l2-2
			p8 = 6-x
			p8 = p8*8
			paths.append(2)
		if x < 0:
			p8 = 4*p8
			p8 = x*8
			p8 = l2-7
			paths.append(3)
		else:
			l2 = l2-1
			x = l2*p8
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