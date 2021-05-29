import numpy as np 

def function(x):

	l6 = 4
	p0 = x
	paths = []
	try:
		if x > 4:
			x = x+x
			l6 = l6+9
			paths.append(1)
		else:
			l6 = l6/x
			l6 = l6+0
			x = 2/l6
			paths.append(2)
		if p0 >= 3:
			l6 = l6+5
			paths.append(3)
		else:
			p0 = 6-p0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))