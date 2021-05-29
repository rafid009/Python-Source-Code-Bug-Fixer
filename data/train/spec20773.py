import numpy as np 

def function(x):

	a9 = 5
	j9 = 7
	paths = []
	try:
		if x > 7:
			a9 = a9+x
			paths.append(1)
		else:
			a9 = a9+4
			paths.append(2)
		if x < 0:
			x = x/a9
			a9 = a9-x
			j9 = j9-9
			paths.append(3)
		else:
			x = x*2
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