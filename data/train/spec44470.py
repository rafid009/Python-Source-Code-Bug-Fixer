import numpy as np 

def function(x):

	v5 = x
	j7 = 7
	paths = []
	try:
		if j7 < 3:
			v5 = j7/x
			paths.append(1)
		else:
			v5 = v5+9
			x = x+7
			paths.append(2)
		if j7 >= 4:
			x = v5+v5
			j7 = 8*9
			paths.append(3)
		else:
			v5 = 7-v5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))