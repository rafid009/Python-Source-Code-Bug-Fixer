import numpy as np 

def function(x):

	e3 = 8
	p3 = 4
	paths = []
	try:
		if p3 > 5:
			p3 = p3/4
			paths.append(1)
		else:
			e3 = x+7
			x = 6-x
			paths.append(2)
		if p3 < 0:
			e3 = e3/1
			e3 = e3/p3
			p3 = 6-p3
			paths.append(3)
		else:
			x = x*2
			e3 = 0/3
			e3 = e3-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))