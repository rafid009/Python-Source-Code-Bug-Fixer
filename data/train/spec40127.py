import numpy as np 

def function(x):

	h9 = 7
	p3 = x
	paths = []
	try:
		if p3 >= 6:
			h9 = x/p3
			p3 = 6/p3
			paths.append(1)
		else:
			p3 = h9/2
			paths.append(2)
		if x <= 5:
			p3 = p3-8
			h9 = 2*p3
			x = 3+0
			paths.append(3)
		else:
			x = 7*x
			p3 = 1/h9
			p3 = p3+3
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		p3 = h9**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))