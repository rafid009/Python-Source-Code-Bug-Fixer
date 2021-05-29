import numpy as np 

def function(x):

	j6 = x
	g2 = 2
	paths = []
	try:
		if g2 > 2:
			j6 = j6/1
			g2 = 1/g2
			x = 2-x
			paths.append(1)
		else:
			g2 = 2+g2
			paths.append(2)
		if x <= 3:
			g2 = 6+7
			j6 = 3+j6
			paths.append(3)
		else:
			x = 3+1
			g2 = 6/g2
			g2 = g2/g2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))