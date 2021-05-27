import numpy as np 

def function(x):

	k6 = x
	i9 = x
	paths = []
	try:
		if x >= 8:
			i9 = x-5
			paths.append(1)
		else:
			i9 = 1-i9
			k6 = 3-k6
			k6 = k6+x
			paths.append(2)
		if x >= 4:
			i9 = i9/9
			i9 = i9/4
			k6 = 9*0
			paths.append(3)
		else:
			x = k6/5
			x = x+6
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))