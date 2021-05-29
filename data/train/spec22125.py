import numpy as np 

def function(x):

	p7 = x
	e1 = x
	paths = []
	try:
		if p7 > 2:
			e1 = 5+e1
			paths.append(1)
		else:
			e1 = x*e1
			paths.append(2)
		if p7 <= 1:
			e1 = e1-e1
			p7 = 4/5
			e1 = e1-e1
			paths.append(3)
		else:
			p7 = 7*p7
			e1 = x/e1
			p7 = p7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))