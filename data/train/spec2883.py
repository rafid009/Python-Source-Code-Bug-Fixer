import numpy as np 

def function(x):

	j1 = x
	z4 = x
	paths = []
	try:
		if x > 1:
			j1 = z4/4
			j1 = j1/6
			j1 = x*j1
			paths.append(1)
		else:
			j1 = j1+x
			j1 = j1-0
			paths.append(2)
		if j1 >= 5:
			z4 = 3*x
			paths.append(3)
		else:
			z4 = z4+6
			j1 = j1+5
			j1 = 8*j1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		j1 = j1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))