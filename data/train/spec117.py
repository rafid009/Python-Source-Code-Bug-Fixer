import numpy as np 

def function(x):

	a0 = 4
	j1 = x
	paths = []
	try:
		if j1 >= 9:
			x = x+j1
			j1 = 9/1
			x = x+2
			paths.append(1)
		else:
			x = 4+j1
			j1 = x*j1
			j1 = j1*5
			paths.append(2)
		if a0 < 0:
			x = x+x
			a0 = a0-2
			x = 4-8
			paths.append(3)
		else:
			j1 = j1/2
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		a0 = j1**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))