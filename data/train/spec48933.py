import numpy as np 

def function(x):

	g2 = x
	j6 = 3
	paths = []
	try:
		if x < 5:
			x = j6-x
			j6 = j6/5
			paths.append(1)
		else:
			g2 = 3*0
			paths.append(2)
		if j6 >= 1:
			x = j6/j6
			x = g2/x
			paths.append(3)
		else:
			j6 = g2/4
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))