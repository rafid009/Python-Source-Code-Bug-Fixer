import numpy as np 

def function(x):

	q3 = 3
	j3 = 6
	paths = []
	try:
		if j3 <= 9:
			q3 = 8+q3
			j3 = 9/x
			j3 = j3+j3
			paths.append(1)
		else:
			x = 3/5
			paths.append(2)
		if j3 < 2:
			j3 = j3/1
			x = j3+9
			j3 = j3+4
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))