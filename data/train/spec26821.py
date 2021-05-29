import numpy as np 

def function(x):

	p2 = x
	l6 = 6
	x = 0
	paths = []
	try:
		if p2 > 0:
			p2 = x-2
			x = p2/3
			paths.append(1)
		else:
			l6 = l6*x
			x = x*1
			x = x/6
			paths.append(2)
		if l6 > 1:
			p2 = 6-5
			paths.append(3)
		else:
			p2 = 6+p2
			x = 7-p2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))