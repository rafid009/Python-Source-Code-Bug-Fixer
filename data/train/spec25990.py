import numpy as np 

def function(x):

	p7 = 4
	a1 = 5
	paths = []
	try:
		if a1 < 1:
			a1 = 9-p7
			x = x+4
			x = x+p7
			paths.append(1)
		else:
			p7 = x/2
			x = x*a1
			x = x-6
			paths.append(2)
		if x < 9:
			x = x/6
			paths.append(3)
		else:
			a1 = a1-6
			p7 = p7+9
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		a1 = p7**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))