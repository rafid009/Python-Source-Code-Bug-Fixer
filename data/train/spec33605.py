import numpy as np 

def function(x):

	j6 = 7
	a9 = 6
	paths = []
	try:
		if j6 >= 4:
			a9 = 5/a9
			paths.append(1)
		else:
			a9 = a9*j6
			paths.append(2)
		if a9 > 5:
			j6 = 9/x
			j6 = 6-7
			a9 = 1/9
			paths.append(3)
		else:
			j6 = j6-9
			a9 = 7/a9
			a9 = j6+x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		j6 = a9**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))