import numpy as np 

def function(x):

	j1 = 4
	a5 = 0
	x = x
	paths = []
	try:
		if j1 > 0:
			x = 9*x
			a5 = a5/2
			x = x+a5
			paths.append(1)
		else:
			j1 = x-j1
			x = a5+x
			paths.append(2)
		if x <= 1:
			j1 = j1+7
			paths.append(3)
		else:
			a5 = 0*a5
			a5 = a5-1
			j1 = 1/a5
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