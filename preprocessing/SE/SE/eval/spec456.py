import numpy as np 

def function(x):

	p6 = 7
	b6 = x
	paths = []
	try:
		if x > 4:
			p6 = p6+2
			x = x*9
			p6 = 4+p6
			paths.append(1)
		else:
			x = x-4
			p6 = p6/p6
			p6 = 5*p6
			paths.append(2)
		if x <= 8:
			x = 3*x
			b6 = 6*b6
			paths.append(3)
		else:
			b6 = b6*3
			b6 = 2/3
			p6 = p6/2
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		p6 = b6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))