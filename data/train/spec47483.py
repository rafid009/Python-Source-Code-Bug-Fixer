import numpy as np 

def function(x):

	j3 = x
	x1 = 2
	paths = []
	try:
		if j3 >= 0:
			x1 = x1-5
			paths.append(1)
		else:
			x1 = j3+2
			j3 = x1+j3
			j3 = 3+8
			paths.append(2)
		if x >= 8:
			j3 = 0-j3
			x1 = x1+x
			paths.append(3)
		else:
			x = 4/x
			j3 = 0/x
			x1 = x1*1
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))