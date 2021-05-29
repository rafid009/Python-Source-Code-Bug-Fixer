import numpy as np 

def function(x):

	g3 = 6
	j9 = x
	paths = []
	try:
		if j9 <= 3:
			j9 = 0*x
			j9 = g3+x
			paths.append(1)
		else:
			g3 = 3+6
			paths.append(2)
		if x < 3:
			x = x+8
			j9 = j9*5
			paths.append(3)
		else:
			g3 = g3+2
			g3 = j9-7
			x = x/j9
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))