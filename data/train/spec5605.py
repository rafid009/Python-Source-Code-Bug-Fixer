import numpy as np 

def function(x):

	j2 = x
	i7 = 2
	paths = []
	try:
		if x < 3:
			j2 = j2-2
			paths.append(1)
		else:
			i7 = i7-0
			paths.append(2)
		if i7 >= 2:
			i7 = i7/8
			paths.append(3)
		else:
			i7 = 5-i7
			x = j2-4
			j2 = 8/x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		i7 = j2**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))