import numpy as np 

def function(x):

	j6 = x
	i1 = x
	paths = []
	try:
		if x > 4:
			j6 = x/6
			x = i1-9
			paths.append(1)
		else:
			x = x+i1
			j6 = j6+1
			j6 = 0-j6
			paths.append(2)
		if x >= 9:
			j6 = 3-j6
			paths.append(3)
		else:
			j6 = i1-i1
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