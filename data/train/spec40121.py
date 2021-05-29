import numpy as np 

def function(x):

	p0 = 8
	l4 = 6
	paths = []
	try:
		if x < 7:
			p0 = 7-2
			p0 = 0+p0
			x = 1/l4
			paths.append(1)
		else:
			x = 8+1
			l4 = l4/3
			p0 = 5-p0
			paths.append(2)
		if x <= 1:
			x = x*p0
			paths.append(3)
		else:
			x = l4+5
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))