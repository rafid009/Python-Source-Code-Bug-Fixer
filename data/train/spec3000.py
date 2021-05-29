import numpy as np 

def function(x):

	y7 = 4
	i1 = 2
	paths = []
	try:
		if y7 <= 8:
			y7 = 1-x
			i1 = i1-4
			x = 7-x
			paths.append(1)
		else:
			y7 = i1*i1
			i1 = i1/8
			i1 = i1*0
			paths.append(2)
		if i1 >= 1:
			x = 1*x
			y7 = y7/y7
			paths.append(3)
		else:
			i1 = i1-y7
			i1 = 6+i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))