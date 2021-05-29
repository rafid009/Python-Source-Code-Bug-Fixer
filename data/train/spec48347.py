import numpy as np 

def function(x):

	l3 = 9
	i9 = x
	paths = []
	try:
		if i9 <= 5:
			x = i9*0
			paths.append(1)
		else:
			i9 = 7/9
			i9 = 2-i9
			l3 = 1-6
			paths.append(2)
		if i9 <= 5:
			l3 = 8-5
			paths.append(3)
		else:
			l3 = 7-l3
			l3 = l3/l3
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))