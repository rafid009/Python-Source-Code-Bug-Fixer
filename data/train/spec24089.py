import numpy as np 

def function(x):

	a2 = 0
	p0 = 6
	paths = []
	try:
		if x > 7:
			x = x*0
			x = x+x
			paths.append(1)
		else:
			a2 = a2*a2
			a2 = a2/4
			x = a2-p0
			paths.append(2)
		if x < 4:
			a2 = 8/9
			p0 = 0-p0
			a2 = p0*3
			paths.append(3)
		else:
			p0 = 8*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))