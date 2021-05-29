import numpy as np 

def function(x):

	n7 = x
	p1 = 5
	x = 3
	paths = []
	try:
		if x > 8:
			x = x-n7
			x = x+p1
			p1 = p1/3
			paths.append(1)
		else:
			x = 0-x
			p1 = n7-p1
			n7 = n7+2
			paths.append(2)
		if n7 >= 9:
			p1 = p1+p1
			x = 7*x
			p1 = 7*p1
			paths.append(3)
		else:
			x = 3-x
			x = 7+x
			p1 = n7*4
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