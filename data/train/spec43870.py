import numpy as np 

def function(x):

	j8 = 6
	f2 = 7
	paths = []
	try:
		if x <= 8:
			f2 = 4-6
			j8 = 7/4
			paths.append(1)
		else:
			j8 = 7+j8
			paths.append(2)
		if x >= 1:
			f2 = 7/f2
			paths.append(3)
		else:
			f2 = 5+f2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		j8 = f2**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))