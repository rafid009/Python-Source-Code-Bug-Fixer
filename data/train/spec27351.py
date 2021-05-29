import numpy as np 

def function(x):

	j1 = 9
	i6 = x
	paths = []
	try:
		if j1 >= 9:
			j1 = 3-j1
			paths.append(1)
		else:
			i6 = j1*0
			paths.append(2)
		if x > 0:
			j1 = j1*4
			i6 = i6-i6
			x = j1/x
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))