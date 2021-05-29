import numpy as np 

def function(x):

	p1 = x
	e3 = 7
	paths = []
	try:
		if e3 > 7:
			x = x/5
			x = 0*x
			x = p1+x
			paths.append(1)
		else:
			e3 = x*6
			x = e3-x
			paths.append(2)
		if p1 > 5:
			e3 = e3*9
			x = 9/x
			e3 = 5-6
			paths.append(3)
		else:
			x = x+e3
			p1 = 5-p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))