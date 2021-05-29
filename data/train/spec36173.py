import numpy as np 

def function(x):

	p1 = x
	a2 = 3
	x = x
	paths = []
	try:
		if x > 9:
			p1 = 8-1
			x = a2-x
			a2 = a2+p1
			paths.append(1)
		else:
			a2 = a2-1
			a2 = p1/7
			p1 = a2*p1
			paths.append(2)
		if x >= 4:
			a2 = a2/3
			p1 = p1/x
			paths.append(3)
		else:
			a2 = a2-7
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		p1 = a2**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))