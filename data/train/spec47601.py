import numpy as np 

def function(x):

	p9 = 6
	p3 = x
	paths = []
	try:
		if p9 < 3:
			x = x/7
			paths.append(1)
		else:
			p9 = p9/x
			paths.append(2)
		if p3 >= 2:
			x = 8*x
			paths.append(3)
		else:
			x = x+p9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p3 = p9**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))