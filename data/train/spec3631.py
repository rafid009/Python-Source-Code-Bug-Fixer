import numpy as np 

def function(x):

	x7 = x
	p7 = 9
	paths = []
	try:
		if p7 <= 7:
			x7 = x7/8
			p7 = 8-p7
			x = x-5
			paths.append(1)
		else:
			p7 = p7+1
			p7 = 9/6
			paths.append(2)
		if p7 > 6:
			p7 = p7/9
			x7 = x7*7
			p7 = 6+6
			paths.append(3)
		else:
			x = 7-x
			p7 = p7-0
			x7 = x7+p7
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