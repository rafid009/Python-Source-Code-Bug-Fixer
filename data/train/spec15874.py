import numpy as np 

def function(x):

	p4 = 0
	g4 = x
	paths = []
	try:
		if p4 < 0:
			g4 = g4-1
			p4 = g4/7
			paths.append(1)
		else:
			p4 = 7-8
			g4 = g4*2
			paths.append(2)
		if x <= 0:
			g4 = x+p4
			paths.append(3)
		else:
			p4 = 9/4
			p4 = 7*p4
			p4 = g4*p4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))