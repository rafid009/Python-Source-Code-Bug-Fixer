import numpy as np 

def function(x):

	k4 = 5
	j6 = x
	paths = []
	try:
		if k4 >= 1:
			k4 = 6/1
			x = x*3
			paths.append(1)
		else:
			k4 = 0+9
			j6 = j6-0
			paths.append(2)
		if x < 2:
			j6 = j6+1
			j6 = x+j6
			paths.append(3)
		else:
			x = k4/9
			k4 = j6/j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		k4 = j6**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))