import numpy as np 

def function(x):

	p4 = x
	j1 = 1
	paths = []
	try:
		if p4 < 4:
			x = 5-x
			x = 9/x
			paths.append(1)
		else:
			j1 = 7-j1
			x = x/8
			paths.append(2)
		if p4 < 0:
			p4 = p4/4
			paths.append(3)
		else:
			p4 = x+p4
			p4 = p4+0
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