import numpy as np 

def function(x):

	i3 = x
	g2 = 9
	paths = []
	try:
		if i3 >= 0:
			i3 = i3+x
			i3 = 0+i3
			i3 = x+i3
			paths.append(1)
		else:
			g2 = g2*7
			x = x-4
			g2 = g2+0
			paths.append(2)
		if i3 > 8:
			x = 7+x
			i3 = 8+i3
			x = i3*8
			paths.append(3)
		else:
			i3 = x*i3
			i3 = 6*5
			i3 = i3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))