import numpy as np 

def function(x):

	z4 = x
	j3 = 9
	x = 2
	paths = []
	try:
		if x <= 2:
			x = x-9
			j3 = x*j3
			paths.append(1)
		else:
			z4 = z4*2
			z4 = z4*j3
			paths.append(2)
		if j3 < 3:
			j3 = j3*8
			j3 = 5/j3
			paths.append(3)
		else:
			x = x-4
			z4 = z4/z4
			j3 = j3/4
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