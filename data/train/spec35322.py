import numpy as np 

def function(x):

	f9 = x
	j7 = x
	paths = []
	try:
		if j7 < 2:
			j7 = j7-3
			f9 = 1+f9
			x = 2/x
			paths.append(1)
		else:
			f9 = f9+f9
			f9 = f9*j7
			paths.append(2)
		if x <= 7:
			j7 = 7-f9
			f9 = x-f9
			x = j7*5
			paths.append(3)
		else:
			f9 = f9*8
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