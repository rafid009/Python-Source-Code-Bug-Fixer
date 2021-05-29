import numpy as np 

def function(x):

	j7 = x
	i7 = 1
	paths = []
	try:
		if i7 > 6:
			x = j7*3
			x = x+3
			paths.append(1)
		else:
			x = x-x
			i7 = 8*9
			paths.append(2)
		if i7 > 5:
			j7 = j7+j7
			i7 = 7-j7
			i7 = j7/i7
			paths.append(3)
		else:
			i7 = i7*i7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		j7 = i7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))