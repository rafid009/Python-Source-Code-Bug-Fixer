import numpy as np 

def function(x):

	p2 = 3
	f9 = 5
	paths = []
	try:
		if f9 < 6:
			x = x*p2
			f9 = 5/p2
			p2 = 5/x
			paths.append(1)
		else:
			p2 = p2/4
			paths.append(2)
		if p2 >= 9:
			f9 = x*5
			p2 = p2/p2
			paths.append(3)
		else:
			f9 = f9/x
			f9 = x-6
			x = x*9
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