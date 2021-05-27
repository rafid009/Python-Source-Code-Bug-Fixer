import numpy as np 

def function(x):

	l8 = 9
	j1 = x
	paths = []
	try:
		if x < 0:
			j1 = 6-9
			j1 = j1+j1
			paths.append(1)
		else:
			x = x/2
			j1 = 1-j1
			x = 7/x
			paths.append(2)
		if x <= 7:
			l8 = j1+3
			x = 2+9
			j1 = x/1
			paths.append(3)
		else:
			l8 = 6+5
			x = x+l8
			j1 = 5*j1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		l8 = j1**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))