import numpy as np 

def function(x):

	p4 = 2
	a5 = 1
	paths = []
	try:
		if a5 >= 3:
			p4 = x-p4
			a5 = a5+p4
			paths.append(1)
		else:
			a5 = 9/3
			paths.append(2)
		if x <= 5:
			p4 = p4+p4
			a5 = x+6
			paths.append(3)
		else:
			x = p4-4
			a5 = p4+0
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))