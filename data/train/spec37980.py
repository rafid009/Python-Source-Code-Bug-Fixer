import numpy as np 

def function(x):

	j6 = x
	j2 = 8
	paths = []
	try:
		if x > 5:
			j6 = 4+j6
			j2 = 0+j2
			j2 = 4+j6
			paths.append(1)
		else:
			j2 = 2-j2
			j2 = j2-x
			x = x-7
			paths.append(2)
		if j6 > 3:
			j6 = j6+7
			paths.append(3)
		else:
			j6 = j6-3
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j2 = j6**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))