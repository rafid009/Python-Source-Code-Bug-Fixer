import numpy as np 

def function(x):

	j8 = x
	g3 = x
	paths = []
	try:
		if g3 <= 7:
			x = x-3
			x = 0-x
			paths.append(1)
		else:
			g3 = g3/3
			x = 7+x
			x = 6/x
			paths.append(2)
		if j8 > 3:
			j8 = j8*6
			x = x+2
			g3 = g3*x
			paths.append(3)
		else:
			g3 = 3+j8
			j8 = j8-7
			j8 = 7-9
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		j8 = g3**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))