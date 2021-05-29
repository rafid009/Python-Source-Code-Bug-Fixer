import numpy as np 

def function(x):

	p0 = x
	q7 = 8
	paths = []
	try:
		if p0 <= 0:
			x = x+3
			paths.append(1)
		else:
			q7 = 4/9
			paths.append(2)
		if p0 < 4:
			p0 = 5*x
			paths.append(3)
		else:
			x = x*p0
			p0 = 1/5
			x = x/5
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))