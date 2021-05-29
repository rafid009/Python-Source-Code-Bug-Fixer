import numpy as np 

def function(x):

	q5 = 5
	p2 = x
	x = 3
	paths = []
	try:
		if x >= 5:
			x = x+x
			paths.append(1)
		else:
			q5 = p2*3
			p2 = q5*6
			x = x*p2
			paths.append(2)
		if x >= 4:
			p2 = p2/7
			q5 = x-9
			paths.append(3)
		else:
			q5 = q5/x
			x = p2*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))