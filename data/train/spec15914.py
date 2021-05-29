import numpy as np 

def function(x):

	g8 = x
	j3 = 5
	paths = []
	try:
		if g8 >= 9:
			x = x/9
			x = x/5
			x = 6+x
			paths.append(1)
		else:
			j3 = j3/j3
			j3 = 3/g8
			g8 = 1+g8
			paths.append(2)
		if x <= 6:
			g8 = g8-6
			paths.append(3)
		else:
			g8 = 1/3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))