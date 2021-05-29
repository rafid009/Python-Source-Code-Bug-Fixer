import numpy as np 

def function(x):

	n6 = x
	p9 = 8
	x = 0
	paths = []
	try:
		if x >= 4:
			x = 1/x
			paths.append(1)
		else:
			p9 = 1*p9
			paths.append(2)
		if x > 3:
			n6 = n6*7
			x = x+6
			n6 = p9/4
			paths.append(3)
		else:
			p9 = x-n6
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))