import numpy as np 

def function(x):

	j4 = 3
	i1 = 0
	paths = []
	try:
		if j4 > 1:
			j4 = 3+8
			paths.append(1)
		else:
			i1 = 8/i1
			j4 = 2*j4
			j4 = i1-4
			paths.append(2)
		if i1 > 5:
			x = i1*x
			paths.append(3)
		else:
			x = x/2
			i1 = i1-j4
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		j4 = i1**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))