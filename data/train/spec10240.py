import numpy as np 

def function(x):

	z2 = 1
	j9 = 7
	paths = []
	try:
		if j9 >= 6:
			x = 6-3
			j9 = z2+z2
			paths.append(1)
		else:
			z2 = z2+x
			x = 8/7
			z2 = 3-0
			paths.append(2)
		if j9 < 7:
			j9 = 9*j9
			j9 = z2-4
			paths.append(3)
		else:
			j9 = j9*6
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