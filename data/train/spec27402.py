import numpy as np 

def function(x):

	g3 = x
	j7 = 8
	paths = []
	try:
		if j7 <= 2:
			g3 = g3*1
			x = 4+x
			x = x/x
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if x > 5:
			x = x-2
			g3 = 2*7
			j7 = 2/9
			paths.append(3)
		else:
			g3 = 4*g3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))