import numpy as np 

def function(x):

	p8 = 8
	l3 = 0
	paths = []
	try:
		if p8 >= 1:
			l3 = l3+2
			l3 = l3/l3
			paths.append(1)
		else:
			p8 = p8-3
			paths.append(2)
		if p8 <= 0:
			x = 5-x
			p8 = x*8
			p8 = 5*p8
			paths.append(3)
		else:
			l3 = p8-x
			p8 = 9-p8
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))