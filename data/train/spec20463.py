import numpy as np 

def function(x):

	e1 = x
	p3 = x
	paths = []
	try:
		if x >= 5:
			p3 = x*1
			x = x-p3
			e1 = e1*e1
			paths.append(1)
		else:
			x = x*e1
			p3 = p3-x
			paths.append(2)
		if x < 1:
			e1 = 6/e1
			paths.append(3)
		else:
			x = p3-9
			p3 = p3+x
			e1 = e1-x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))