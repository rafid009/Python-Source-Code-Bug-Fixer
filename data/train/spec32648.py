import numpy as np 

def function(x):

	e1 = 5
	i9 = 3
	paths = []
	try:
		if e1 <= 3:
			i9 = i9*0
			i9 = i9-8
			paths.append(1)
		else:
			i9 = i9*7
			i9 = 0+5
			paths.append(2)
		if x > 5:
			e1 = x-e1
			i9 = 8-x
			x = x/i9
			paths.append(3)
		else:
			i9 = i9-0
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))