import numpy as np 

def function(x):

	b8 = x
	p1 = x
	paths = []
	try:
		if p1 <= 6:
			x = x*5
			paths.append(1)
		else:
			x = 2-x
			p1 = 8/8
			paths.append(2)
		if b8 >= 0:
			x = p1*0
			p1 = p1+p1
			paths.append(3)
		else:
			x = x-x
			x = x-8
			p1 = 7*p1
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