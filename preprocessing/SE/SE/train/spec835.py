import numpy as np 

def function(x):

	p4 = 7
	g4 = 1
	paths = []
	try:
		if g4 < 4:
			p4 = g4-6
			x = x*7
			p4 = g4/p4
			paths.append(1)
		else:
			g4 = g4+8
			p4 = p4+p4
			paths.append(2)
		if x < 8:
			x = 0-x
			g4 = p4*g4
			paths.append(3)
		else:
			x = 9*g4
			x = x+6
			p4 = p4*p4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		p4 = g4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))