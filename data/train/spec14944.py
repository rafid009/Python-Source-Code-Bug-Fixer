import numpy as np 

def function(x):

	u1 = x
	j3 = x
	paths = []
	try:
		if u1 >= 7:
			j3 = u1-9
			j3 = j3-u1
			u1 = u1-j3
			paths.append(1)
		else:
			x = u1/3
			paths.append(2)
		if u1 >= 6:
			x = x/x
			paths.append(3)
		else:
			x = j3+u1
			j3 = u1/9
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		j3 = u1**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))