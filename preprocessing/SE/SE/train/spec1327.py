import numpy as np 

def function(x):

	f7 = x
	j1 = x
	paths = []
	try:
		if j1 > 4:
			j1 = 3-j1
			j1 = 9/j1
			paths.append(1)
		else:
			j1 = j1+x
			f7 = x+f7
			paths.append(2)
		if f7 > 4:
			x = 4-x
			j1 = 9/j1
			paths.append(3)
		else:
			j1 = 6-j1
			j1 = j1+6
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