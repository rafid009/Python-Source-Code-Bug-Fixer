import numpy as np 

def function(x):

	l9 = 8
	p0 = 9
	paths = []
	try:
		if x > 6:
			x = x+1
			l9 = 6*7
			p0 = 1*4
			paths.append(1)
		else:
			p0 = 0-p0
			paths.append(2)
		if p0 > 4:
			l9 = l9*7
			paths.append(3)
		else:
			l9 = 7-6
			x = x/l9
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