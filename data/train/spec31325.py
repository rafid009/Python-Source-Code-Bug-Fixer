import numpy as np 

def function(x):

	n1 = 2
	p8 = 8
	paths = []
	try:
		if p8 < 3:
			p8 = x*p8
			paths.append(1)
		else:
			n1 = 7+n1
			x = n1+x
			n1 = n1/x
			paths.append(2)
		if p8 < 2:
			p8 = 2-0
			p8 = n1/4
			paths.append(3)
		else:
			p8 = p8*7
			p8 = p8-p8
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))