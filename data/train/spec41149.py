import numpy as np 

def function(x):

	b7 = 4
	j1 = x
	paths = []
	try:
		if x > 4:
			x = 8*x
			b7 = b7/b7
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if b7 >= 3:
			j1 = j1-0
			paths.append(3)
		else:
			j1 = j1/3
			b7 = b7-4
			x = 7+4
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		j1 = b7**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))