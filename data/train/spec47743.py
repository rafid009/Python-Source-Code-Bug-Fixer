import numpy as np 

def function(x):

	j5 = x
	j7 = 8
	paths = []
	try:
		if x < 8:
			j7 = j7/7
			j7 = j7-x
			paths.append(1)
		else:
			x = j7/3
			paths.append(2)
		if x > 4:
			j7 = j7+8
			j7 = 6+0
			paths.append(3)
		else:
			j7 = x*3
			x = j7+x
			j7 = 9-9
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j7 = j5**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))