import numpy as np 

def function(x):

	a2 = x
	j9 = x
	paths = []
	try:
		if a2 > 5:
			x = x/6
			x = x*7
			paths.append(1)
		else:
			a2 = 7/a2
			j9 = 2/j9
			j9 = j9/x
			paths.append(2)
		if a2 > 7:
			j9 = j9-6
			a2 = j9-a2
			paths.append(3)
		else:
			a2 = a2/x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		j9 = a2**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))