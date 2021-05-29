import numpy as np 

def function(x):

	j5 = 0
	z7 = x
	paths = []
	try:
		if x > 5:
			x = 8/x
			z7 = 4/z7
			x = z7-z7
			paths.append(1)
		else:
			j5 = j5+x
			paths.append(2)
		if x > 4:
			x = j5+x
			j5 = x*6
			paths.append(3)
		else:
			x = 9/6
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		j5 = z7**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))