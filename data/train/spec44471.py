import numpy as np 

def function(x):

	g9 = 0
	i5 = x
	paths = []
	try:
		if g9 <= 9:
			x = x+1
			x = x*5
			paths.append(1)
		else:
			i5 = 6*i5
			g9 = g9*1
			x = x-0
			paths.append(2)
		if g9 >= 3:
			g9 = g9*g9
			g9 = 1*5
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))