import numpy as np 

def function(x):

	k5 = x
	j3 = 9
	paths = []
	try:
		if x < 6:
			k5 = j3+7
			j3 = x+0
			k5 = 3-j3
			paths.append(1)
		else:
			k5 = 8+k5
			x = k5/x
			paths.append(2)
		if k5 < 8:
			x = x+2
			paths.append(3)
		else:
			j3 = 7+4
			x = 9-x
			k5 = 6-j3
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