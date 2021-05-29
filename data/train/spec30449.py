import numpy as np 

def function(x):

	p1 = 0
	g2 = 0
	paths = []
	try:
		if p1 > 6:
			g2 = x/p1
			x = x*8
			p1 = p1/p1
			paths.append(1)
		else:
			g2 = g2-7
			paths.append(2)
		if g2 <= 3:
			p1 = 0-1
			paths.append(3)
		else:
			p1 = p1*0
			g2 = 5+g2
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))