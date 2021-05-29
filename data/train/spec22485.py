import numpy as np 

def function(x):

	j6 = x
	f1 = 2
	x = 9
	paths = []
	try:
		if j6 >= 2:
			f1 = f1/1
			j6 = 4/7
			paths.append(1)
		else:
			j6 = j6+2
			paths.append(2)
		if x >= 9:
			x = 2-x
			paths.append(3)
		else:
			f1 = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))