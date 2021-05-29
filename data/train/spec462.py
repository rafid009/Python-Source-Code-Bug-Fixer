import numpy as np 

def function(x):

	i5 = 7
	g3 = 8
	x = x
	paths = []
	try:
		if g3 <= 0:
			i5 = i5*3
			paths.append(1)
		else:
			i5 = i5*5
			i5 = x*5
			x = x/9
			paths.append(2)
		if i5 > 7:
			i5 = i5*4
			i5 = 5/2
			g3 = 8-2
			paths.append(3)
		else:
			x = x*7
			x = x-9
			g3 = 3/5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		g3 = i5**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))