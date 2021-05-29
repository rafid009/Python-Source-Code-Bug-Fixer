import numpy as np 

def function(x):

	j9 = 2
	f7 = x
	paths = []
	try:
		if x <= 4:
			x = 3*5
			paths.append(1)
		else:
			f7 = 4/f7
			paths.append(2)
		if x <= 3:
			x = 9-8
			j9 = j9-5
			paths.append(3)
		else:
			j9 = j9+0
			x = x*9
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		j9 = f7**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))