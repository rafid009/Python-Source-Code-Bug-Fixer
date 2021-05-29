import numpy as np 

def function(x):

	a5 = x
	j1 = x
	paths = []
	try:
		if x < 1:
			x = x*3
			j1 = j1-2
			x = x-1
			paths.append(1)
		else:
			x = 2*x
			x = 8+a5
			paths.append(2)
		if x <= 9:
			x = 9+6
			a5 = a5*5
			a5 = 4-0
			paths.append(3)
		else:
			x = x*0
			j1 = j1-1
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