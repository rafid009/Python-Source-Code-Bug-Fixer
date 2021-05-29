import numpy as np 

def function(x):

	g3 = 8
	j5 = 4
	paths = []
	try:
		if g3 >= 5:
			j5 = j5+x
			g3 = j5/9
			j5 = 3-3
			paths.append(1)
		else:
			g3 = g3/6
			j5 = j5*2
			paths.append(2)
		if j5 < 9:
			x = g3-x
			paths.append(3)
		else:
			x = 9/x
			g3 = 1*1
			j5 = j5*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))