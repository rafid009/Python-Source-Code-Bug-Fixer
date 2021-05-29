import numpy as np 

def function(x):

	g2 = 9
	l5 = x
	paths = []
	try:
		if l5 > 9:
			l5 = x-l5
			x = l5/3
			paths.append(1)
		else:
			l5 = l5+2
			l5 = l5+8
			paths.append(2)
		if g2 < 5:
			g2 = x+9
			paths.append(3)
		else:
			l5 = l5-0
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))