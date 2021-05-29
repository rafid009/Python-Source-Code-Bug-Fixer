import numpy as np 

def function(x):

	j5 = x
	u1 = x
	paths = []
	try:
		if x <= 8:
			x = x+j5
			paths.append(1)
		else:
			j5 = 8+5
			u1 = 3-u1
			u1 = u1-u1
			paths.append(2)
		if x > 2:
			j5 = 8/6
			paths.append(3)
		else:
			j5 = 1+j5
			j5 = 2+0
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		j5 = u1**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))