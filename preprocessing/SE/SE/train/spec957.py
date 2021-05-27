import numpy as np 

def function(x):

	b6 = x
	i1 = 9
	paths = []
	try:
		if x > 1:
			b6 = 4/x
			b6 = 7/i1
			b6 = b6-i1
			paths.append(1)
		else:
			x = 4+3
			paths.append(2)
		if i1 >= 5:
			x = 8-x
			i1 = x+7
			x = b6-b6
			paths.append(3)
		else:
			i1 = i1-x
			b6 = b6+x
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