import numpy as np 

def function(x):

	w9 = x
	j1 = 5
	paths = []
	try:
		if x < 5:
			j1 = w9/3
			x = x/x
			paths.append(1)
		else:
			x = 5+x
			x = 6-5
			paths.append(2)
		if j1 >= 2:
			j1 = 6+j1
			w9 = w9-j1
			paths.append(3)
		else:
			j1 = w9+0
			x = 1-8
			w9 = j1+3
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		j1 = j1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))