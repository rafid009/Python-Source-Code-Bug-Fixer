import numpy as np 

def function(x):

	w9 = 7
	j7 = x
	paths = []
	try:
		if j7 > 5:
			w9 = w9-x
			paths.append(1)
		else:
			j7 = 2/j7
			j7 = j7/1
			j7 = x+w9
			paths.append(2)
		if w9 > 2:
			w9 = x*7
			j7 = 9+j7
			paths.append(3)
		else:
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		j7 = w9**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))