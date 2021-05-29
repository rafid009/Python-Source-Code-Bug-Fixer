import numpy as np 

def function(x):

	p1 = 5
	p6 = x
	paths = []
	try:
		if p6 <= 2:
			p1 = p1/9
			p6 = p6+9
			paths.append(1)
		else:
			x = x*4
			p6 = p6*8
			paths.append(2)
		if p1 <= 5:
			p6 = 9-p6
			p6 = p6*1
			p1 = 7*4
			paths.append(3)
		else:
			p6 = 6-9
			x = p6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))