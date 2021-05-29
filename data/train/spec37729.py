import numpy as np 

def function(x):

	p1 = 6
	a4 = x
	paths = []
	try:
		if p1 > 4:
			p1 = 6*0
			paths.append(1)
		else:
			x = 8+3
			a4 = x-a4
			x = 8-8
			paths.append(2)
		if a4 >= 4:
			x = 8*4
			paths.append(3)
		else:
			a4 = a4/7
			p1 = 3*2
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