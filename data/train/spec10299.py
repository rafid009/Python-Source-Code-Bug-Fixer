import numpy as np 

def function(x):

	j1 = 6
	f7 = x
	x = x
	paths = []
	try:
		if x <= 5:
			j1 = 2-j1
			x = 8*x
			paths.append(1)
		else:
			j1 = 3/j1
			paths.append(2)
		if x > 3:
			x = 3+7
			j1 = j1/4
			paths.append(3)
		else:
			j1 = j1/5
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		j1 = f7**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))