import numpy as np 

def function(x):

	u7 = x
	j1 = 8
	paths = []
	try:
		if u7 >= 8:
			j1 = 4-4
			j1 = 4-6
			paths.append(1)
		else:
			u7 = u7/3
			paths.append(2)
		if x > 4:
			j1 = 4*j1
			paths.append(3)
		else:
			u7 = j1+9
			j1 = j1-0
			j1 = 5/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))