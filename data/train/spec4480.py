import numpy as np 

def function(x):

	e9 = x
	p7 = 4
	paths = []
	try:
		if e9 > 0:
			p7 = p7+1
			paths.append(1)
		else:
			p7 = 3-e9
			p7 = 5*x
			paths.append(2)
		if p7 >= 9:
			e9 = x/p7
			paths.append(3)
		else:
			x = 3+x
			x = e9-x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		p7 = e9**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))