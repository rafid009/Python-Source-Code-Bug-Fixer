import numpy as np 

def function(x):

	w7 = 3
	j1 = x
	paths = []
	try:
		if x >= 8:
			j1 = 5+j1
			paths.append(1)
		else:
			x = x+5
			x = w7-5
			x = x/4
			paths.append(2)
		if w7 > 5:
			w7 = w7*1
			x = x/x
			j1 = 8*j1
			paths.append(3)
		else:
			j1 = j1+4
			x = x+w7
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		w7 = j1**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))