import numpy as np 

def function(x):

	p6 = x
	b5 = x
	paths = []
	try:
		if p6 >= 3:
			p6 = 0/p6
			paths.append(1)
		else:
			x = x*1
			p6 = p6+b5
			paths.append(2)
		if x >= 7:
			x = 3-2
			b5 = b5*5
			p6 = 8-p6
			paths.append(3)
		else:
			p6 = 3*p6
			x = x+1
			b5 = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))