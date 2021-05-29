import numpy as np 

def function(x):

	j9 = x
	e3 = x
	paths = []
	try:
		if e3 < 1:
			j9 = 7+j9
			paths.append(1)
		else:
			e3 = e3*x
			e3 = e3*5
			paths.append(2)
		if x >= 5:
			j9 = j9/4
			paths.append(3)
		else:
			e3 = 4/9
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