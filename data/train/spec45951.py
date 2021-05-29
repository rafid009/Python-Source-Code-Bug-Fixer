import numpy as np 

def function(x):

	j7 = 4
	t0 = x
	paths = []
	try:
		if x > 7:
			x = t0-9
			paths.append(1)
		else:
			t0 = t0-5
			x = 0+3
			paths.append(2)
		if t0 > 8:
			j7 = j7+5
			x = x+1
			j7 = j7-x
			paths.append(3)
		else:
			j7 = j7*j7
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