import numpy as np 

def function(x):

	p7 = x
	g2 = x
	paths = []
	try:
		if g2 <= 0:
			p7 = p7+p7
			g2 = g2*g2
			paths.append(1)
		else:
			p7 = 9/p7
			g2 = g2-0
			paths.append(2)
		if p7 > 8:
			g2 = 0/7
			p7 = x+p7
			paths.append(3)
		else:
			g2 = g2*0
			x = x*x
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))