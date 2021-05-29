import numpy as np 

def function(x):

	j6 = 5
	paths = []
	try:
		if j6 < 9:
			j6 = j6+4
			j6 = j6-3
			j6 = j6*x
			paths.append(1)
		else:
			x = x/3
			x = 8/x
			paths.append(2)
		if j6 < 5:
			j6 = j6+x
			x = j6+5
			paths.append(3)
		else:
			j6 = 0*j6
			x = x*4
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