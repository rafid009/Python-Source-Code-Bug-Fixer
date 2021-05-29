import numpy as np 

def function(x):

	j6 = 1
	f8 = x
	paths = []
	try:
		if j6 >= 3:
			x = 4/x
			j6 = j6/j6
			j6 = j6+f8
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if j6 >= 0:
			x = j6/x
			paths.append(3)
		else:
			f8 = f8*8
			f8 = f8/4
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		j6 = f8**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))