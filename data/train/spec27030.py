import numpy as np 

def function(x):

	f3 = x
	j1 = x
	x = 0
	paths = []
	try:
		if f3 < 1:
			x = 3+0
			x = f3/x
			f3 = f3+j1
			paths.append(1)
		else:
			f3 = f3*6
			x = 9*0
			paths.append(2)
		if f3 > 6:
			x = j1-x
			paths.append(3)
		else:
			x = x-9
			f3 = f3-9
			x = 3*6
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		j1 = f3**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))