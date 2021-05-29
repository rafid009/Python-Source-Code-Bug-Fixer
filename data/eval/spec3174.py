import numpy as np 

def function(x):

	g2 = 0
	j1 = 9
	paths = []
	try:
		if x > 2:
			g2 = 7*g2
			x = g2+6
			paths.append(1)
		else:
			j1 = 6+g2
			paths.append(2)
		if j1 >= 2:
			x = x*x
			x = g2-x
			j1 = j1+3
			paths.append(3)
		else:
			x = g2+x
			j1 = 1*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))