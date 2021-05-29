import numpy as np 

def function(x):

	j3 = 2
	g3 = x
	paths = []
	try:
		if g3 < 8:
			g3 = g3-0
			g3 = 7+g3
			g3 = 2/g3
			paths.append(1)
		else:
			x = x+x
			g3 = x*0
			paths.append(2)
		if j3 < 1:
			j3 = j3+x
			x = 3/g3
			x = 6-x
			paths.append(3)
		else:
			j3 = j3/j3
			j3 = j3-3
			x = x-x
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		j3 = g3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))