import numpy as np 

def function(x):

	t3 = x
	j7 = x
	paths = []
	try:
		if x >= 5:
			x = 1/6
			j7 = j7-t3
			x = 6*x
			paths.append(1)
		else:
			t3 = j7*t3
			x = 0-9
			paths.append(2)
		if j7 < 1:
			j7 = 7*j7
			x = x*x
			paths.append(3)
		else:
			j7 = j7-4
			x = t3+1
			j7 = j7*4
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))