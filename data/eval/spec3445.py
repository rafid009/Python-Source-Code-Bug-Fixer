import numpy as np 

def function(x):

	i6 = x
	j9 = x
	paths = []
	try:
		if j9 <= 9:
			i6 = 7/x
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if x <= 7:
			x = i6/x
			paths.append(3)
		else:
			i6 = j9*3
			j9 = x-j9
			j9 = 5/3
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		i6 = j9**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))