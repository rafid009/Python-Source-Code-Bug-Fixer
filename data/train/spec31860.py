import numpy as np 

def function(x):

	g7 = 0
	i7 = 4
	paths = []
	try:
		if i7 >= 4:
			g7 = g7*3
			g7 = 6-i7
			i7 = i7*i7
			paths.append(1)
		else:
			i7 = i7+2
			paths.append(2)
		if g7 <= 8:
			x = 4*x
			i7 = i7-i7
			i7 = x/7
			paths.append(3)
		else:
			g7 = g7-6
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))