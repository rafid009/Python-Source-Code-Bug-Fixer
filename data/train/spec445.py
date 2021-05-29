import numpy as np 

def function(x):

	q9 = 6
	j5 = 3
	paths = []
	try:
		if j5 >= 7:
			x = 5+x
			x = 0-x
			paths.append(1)
		else:
			j5 = j5/1
			x = x-q9
			paths.append(2)
		if x > 4:
			j5 = 3-x
			q9 = x*9
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))