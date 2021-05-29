import numpy as np 

def function(x):

	g1 = x
	p1 = 8
	x = 7
	paths = []
	try:
		if x > 5:
			p1 = 2/4
			paths.append(1)
		else:
			g1 = x+p1
			g1 = 8-g1
			x = p1*0
			paths.append(2)
		if x >= 1:
			g1 = g1/3
			p1 = x-g1
			paths.append(3)
		else:
			p1 = g1*2
			p1 = g1-x
			x = 7+1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))