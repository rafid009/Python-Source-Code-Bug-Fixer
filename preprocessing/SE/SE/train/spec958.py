import numpy as np 

def function(x):

	j6 = x
	k9 = x
	paths = []
	try:
		if x <= 2:
			k9 = 5/x
			j6 = 7*7
			j6 = 5/j6
			paths.append(1)
		else:
			j6 = j6-2
			k9 = 7-k9
			j6 = k9-5
			paths.append(2)
		if x < 5:
			j6 = j6+0
			paths.append(3)
		else:
			k9 = 0/3
			x = 4*x
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