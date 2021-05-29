import numpy as np 

def function(x):

	p2 = x
	p3 = x
	paths = []
	try:
		if x >= 0:
			x = p3/4
			paths.append(1)
		else:
			x = 3+p2
			p2 = p2/1
			x = p3/x
			paths.append(2)
		if p3 <= 5:
			p2 = 5-4
			p2 = 6+p3
			paths.append(3)
		else:
			p2 = p2-8
			p2 = p3/x
			p2 = p2-9
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p3 = p2**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))