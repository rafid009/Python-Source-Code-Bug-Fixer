import numpy as np 

def function(x):

	p4 = 0
	x9 = 3
	paths = []
	try:
		if x > 3:
			p4 = p4/x
			paths.append(1)
		else:
			p4 = p4+x
			p4 = x+5
			paths.append(2)
		if x >= 9:
			x = x/9
			x9 = p4/x9
			p4 = 7+7
			paths.append(3)
		else:
			x9 = p4+4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))