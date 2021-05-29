import numpy as np 

def function(x):

	j7 = 5
	a7 = x
	paths = []
	try:
		if j7 <= 0:
			x = x+9
			paths.append(1)
		else:
			a7 = a7-x
			a7 = x+4
			a7 = 1+a7
			paths.append(2)
		if j7 < 7:
			x = x*3
			x = 4-x
			j7 = j7-j7
			paths.append(3)
		else:
			x = 3+5
			x = x+8
			j7 = x*a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))