import numpy as np 

def function(x):

	f5 = 0
	p2 = x
	x = x
	paths = []
	try:
		if f5 < 8:
			x = 6+p2
			paths.append(1)
		else:
			p2 = p2+6
			p2 = p2*3
			paths.append(2)
		if f5 >= 9:
			x = x/1
			paths.append(3)
		else:
			f5 = 7+6
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