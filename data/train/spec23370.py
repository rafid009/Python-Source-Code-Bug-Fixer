import numpy as np 

def function(x):

	t6 = x
	j1 = x
	paths = []
	try:
		if t6 >= 3:
			x = 0-1
			paths.append(1)
		else:
			t6 = 0-6
			paths.append(2)
		if t6 > 6:
			t6 = 3+t6
			x = t6-j1
			x = 1*5
			paths.append(3)
		else:
			x = x*7
			j1 = j1*8
			t6 = 5-t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))