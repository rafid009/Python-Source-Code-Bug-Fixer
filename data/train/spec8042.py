import numpy as np 

def function(x):

	j5 = x
	u1 = x
	paths = []
	try:
		if j5 < 1:
			j5 = j5+3
			x = x+u1
			paths.append(1)
		else:
			j5 = 9*3
			paths.append(2)
		if u1 > 3:
			x = u1+1
			u1 = u1+7
			paths.append(3)
		else:
			u1 = u1/2
			u1 = 3/x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))