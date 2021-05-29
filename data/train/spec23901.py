import numpy as np 

def function(x):

	p7 = x
	j7 = 1
	paths = []
	try:
		if j7 >= 6:
			x = x*p7
			p7 = p7-4
			paths.append(1)
		else:
			x = 7-x
			p7 = p7*p7
			x = j7+x
			paths.append(2)
		if j7 <= 3:
			j7 = j7-4
			x = j7/2
			j7 = j7*5
			paths.append(3)
		else:
			j7 = j7/j7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))