import numpy as np 

def function(x):

	j6 = x
	w9 = 6
	paths = []
	try:
		if x < 8:
			x = x-w9
			paths.append(1)
		else:
			w9 = 7+w9
			w9 = x+w9
			paths.append(2)
		if w9 >= 6:
			x = 5/x
			w9 = w9/9
			x = w9+w9
			paths.append(3)
		else:
			j6 = j6-5
			w9 = 6/8
			j6 = 5-j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))