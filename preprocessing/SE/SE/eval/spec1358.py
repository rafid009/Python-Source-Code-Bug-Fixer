import numpy as np 

def function(x):

	e1 = 6
	p2 = x
	paths = []
	try:
		if x >= 3:
			e1 = p2+x
			e1 = 1-p2
			p2 = p2/9
			paths.append(1)
		else:
			e1 = e1/x
			p2 = 7+p2
			e1 = e1+2
			paths.append(2)
		if x > 6:
			p2 = p2*p2
			e1 = 9*e1
			paths.append(3)
		else:
			e1 = 3*e1
			e1 = 3*2
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		p2 = e1**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))