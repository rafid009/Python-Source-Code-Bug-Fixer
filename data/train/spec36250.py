import numpy as np 

def function(x):

	j9 = x
	a0 = 0
	paths = []
	try:
		if x > 5:
			a0 = a0+9
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x >= 6:
			x = x/4
			x = 0+8
			x = 3/x
			paths.append(3)
		else:
			j9 = j9*2
			x = 1*x
			x = j9*x
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))