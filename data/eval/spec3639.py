import numpy as np 

def function(x):

	j5 = x
	z4 = 4
	paths = []
	try:
		if x > 5:
			j5 = j5/j5
			paths.append(1)
		else:
			z4 = x-j5
			z4 = j5-z4
			j5 = j5+2
			paths.append(2)
		if j5 < 8:
			j5 = j5*5
			j5 = 6*9
			j5 = 4*0
			paths.append(3)
		else:
			z4 = 4/2
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		j5 = z4**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))