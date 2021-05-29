import numpy as np 

def function(x):

	j9 = 9
	i1 = x
	paths = []
	try:
		if j9 >= 2:
			j9 = j9*8
			paths.append(1)
		else:
			i1 = 3+i1
			i1 = 0+i1
			x = 8+7
			paths.append(2)
		if j9 > 8:
			i1 = i1-i1
			j9 = 9/5
			paths.append(3)
		else:
			x = i1/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))