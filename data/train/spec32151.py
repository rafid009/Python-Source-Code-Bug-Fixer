import numpy as np 

def function(x):

	j9 = 3
	b3 = x
	paths = []
	try:
		if j9 <= 5:
			x = x/b3
			j9 = j9-7
			paths.append(1)
		else:
			x = j9/x
			b3 = 5-5
			x = b3*8
			paths.append(2)
		if x >= 5:
			j9 = j9*8
			x = x-6
			j9 = 7-2
			paths.append(3)
		else:
			x = b3*7
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))