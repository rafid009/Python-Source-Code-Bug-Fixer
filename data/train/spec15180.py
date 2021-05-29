import numpy as np 

def function(x):

	a4 = x
	j6 = x
	paths = []
	try:
		if j6 < 9:
			j6 = 0+j6
			paths.append(1)
		else:
			j6 = 8*a4
			paths.append(2)
		if a4 > 4:
			j6 = 8-j6
			j6 = a4/3
			paths.append(3)
		else:
			a4 = a4+9
			x = x/1
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))