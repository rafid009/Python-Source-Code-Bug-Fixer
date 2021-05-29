import numpy as np 

def function(x):

	f0 = x
	j7 = 4
	x = 1
	paths = []
	try:
		if x < 3:
			f0 = x+f0
			x = x*9
			paths.append(1)
		else:
			j7 = j7*6
			f0 = 6/f0
			paths.append(2)
		if j7 < 0:
			x = 2/x
			paths.append(3)
		else:
			f0 = 2-f0
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		j7 = f0**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))