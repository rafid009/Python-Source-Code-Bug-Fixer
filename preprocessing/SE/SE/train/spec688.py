import numpy as np 

def function(x):

	p3 = 2
	g6 = x
	paths = []
	try:
		if p3 <= 2:
			x = 2/x
			paths.append(1)
		else:
			p3 = p3-8
			p3 = g6+g6
			x = x*8
			paths.append(2)
		if g6 >= 5:
			x = 4*0
			g6 = 2-6
			g6 = p3-g6
			paths.append(3)
		else:
			p3 = x-6
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))