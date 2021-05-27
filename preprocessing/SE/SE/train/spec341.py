import numpy as np 

def function(x):

	u2 = 6
	j1 = 2
	paths = []
	try:
		if j1 <= 7:
			j1 = j1-4
			u2 = u2/x
			paths.append(1)
		else:
			x = 9*x
			u2 = 1-u2
			x = x+9
			paths.append(2)
		if x > 9:
			x = x*0
			u2 = u2*0
			j1 = j1*3
			paths.append(3)
		else:
			j1 = j1-7
			x = 7/j1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))