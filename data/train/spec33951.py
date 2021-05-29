import numpy as np 

def function(x):

	w2 = 9
	j9 = x
	paths = []
	try:
		if x > 2:
			x = 3+x
			w2 = 6-5
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if x >= 1:
			x = x+j9
			paths.append(3)
		else:
			w2 = 6/x
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