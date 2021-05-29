import numpy as np 

def function(x):

	j5 = 1
	i1 = 3
	paths = []
	try:
		if x >= 0:
			j5 = j5*0
			paths.append(1)
		else:
			j5 = 0-x
			i1 = 1*i1
			paths.append(2)
		if j5 >= 2:
			j5 = i1-0
			j5 = x+5
			i1 = 1-i1
			paths.append(3)
		else:
			j5 = j5-3
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))