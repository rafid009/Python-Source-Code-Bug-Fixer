import numpy as np 

def function(x):

	u1 = x
	j0 = 5
	paths = []
	try:
		if x >= 3:
			j0 = j0*4
			u1 = u1-5
			paths.append(1)
		else:
			u1 = x/u1
			x = x+u1
			x = 2*2
			paths.append(2)
		if j0 >= 5:
			j0 = j0-x
			u1 = u1/j0
			x = x+9
			paths.append(3)
		else:
			x = x*1
			u1 = u1/u1
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))