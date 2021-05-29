import numpy as np 

def function(x):

	n3 = x
	p3 = x
	x = 1
	paths = []
	try:
		if p3 < 2:
			p3 = p3/n3
			n3 = n3/x
			p3 = 8/n3
			paths.append(1)
		else:
			p3 = x/5
			paths.append(2)
		if n3 <= 8:
			p3 = 0+p3
			paths.append(3)
		else:
			p3 = 6/p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))