import numpy as np 

def function(x):

	i6 = x
	j1 = x
	paths = []
	try:
		if x >= 6:
			j1 = 2-8
			x = 8/j1
			paths.append(1)
		else:
			x = 2*6
			i6 = i6+8
			i6 = i6*i6
			paths.append(2)
		if x >= 8:
			j1 = j1*8
			i6 = 4+i6
			paths.append(3)
		else:
			i6 = 3-9
			x = x-6
			j1 = 0/x
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		i6 = j1**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))