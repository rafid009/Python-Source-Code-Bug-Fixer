import numpy as np 

def function(x):

	b9 = 8
	j6 = 2
	paths = []
	try:
		if j6 >= 8:
			b9 = b9+5
			b9 = 0*0
			b9 = 9+7
			paths.append(1)
		else:
			x = x+j6
			x = b9+3
			paths.append(2)
		if b9 >= 5:
			j6 = 3/j6
			b9 = 1-b9
			paths.append(3)
		else:
			b9 = 6/8
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		j6 = b9**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))