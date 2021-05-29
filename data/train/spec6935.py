import numpy as np 

def function(x):

	j1 = x
	l0 = 8
	paths = []
	try:
		if l0 > 8:
			j1 = 3-3
			l0 = l0+l0
			x = x+l0
			paths.append(1)
		else:
			j1 = l0/j1
			j1 = 8/j1
			x = x*4
			paths.append(2)
		if j1 > 7:
			l0 = l0+5
			x = x+l0
			j1 = j1/6
			paths.append(3)
		else:
			x = 4+9
			j1 = 6/j1
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