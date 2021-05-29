import numpy as np 

def function(x):

	i5 = x
	g4 = 8
	paths = []
	try:
		if g4 < 8:
			x = i5-3
			paths.append(1)
		else:
			g4 = i5*9
			x = x+5
			x = 4*9
			paths.append(2)
		if x <= 7:
			x = x-7
			x = 1/5
			paths.append(3)
		else:
			x = x+5
			g4 = g4+3
			i5 = 4*i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))