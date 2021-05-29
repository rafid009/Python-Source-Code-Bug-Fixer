import numpy as np 

def function(x):

	r4 = 3
	p1 = x
	x = 8
	paths = []
	try:
		if x > 2:
			x = x/4
			p1 = p1-p1
			p1 = p1-4
			paths.append(1)
		else:
			x = x*3
			x = x+9
			p1 = p1/p1
			paths.append(2)
		if r4 < 9:
			x = x*p1
			p1 = 9+2
			paths.append(3)
		else:
			x = p1-3
			p1 = p1*0
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