import numpy as np 

def function(x):

	j1 = x
	p4 = x
	paths = []
	try:
		if j1 < 9:
			p4 = p4/j1
			paths.append(1)
		else:
			j1 = p4*4
			p4 = 6-p4
			paths.append(2)
		if j1 >= 8:
			x = 2*7
			p4 = 0-p4
			paths.append(3)
		else:
			p4 = p4+9
			x = x+x
			p4 = p4/j1
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