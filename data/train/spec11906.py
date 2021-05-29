import numpy as np 

def function(x):

	j5 = x
	w3 = x
	paths = []
	try:
		if x > 0:
			w3 = x/3
			w3 = w3/1
			paths.append(1)
		else:
			j5 = j5+5
			j5 = 3-j5
			w3 = 1*w3
			paths.append(2)
		if x < 9:
			j5 = 9-w3
			paths.append(3)
		else:
			j5 = 7+7
			x = x/x
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		j5 = w3**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))