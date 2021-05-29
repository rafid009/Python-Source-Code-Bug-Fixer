import numpy as np 

def function(x):

	j1 = x
	x5 = 4
	paths = []
	try:
		if x5 <= 9:
			x5 = 6+4
			x5 = x+9
			paths.append(1)
		else:
			j1 = 5-j1
			x = x*5
			x5 = x5/x
			paths.append(2)
		if x5 >= 6:
			x = x/x5
			x5 = x5/x
			j1 = x*9
			paths.append(3)
		else:
			x = x+3
			x = 6+x
			x5 = 3+0
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))