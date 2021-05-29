import numpy as np 

def function(x):

	i9 = x
	q2 = x
	paths = []
	try:
		if x > 6:
			q2 = q2+3
			q2 = 8-6
			i9 = 2-i9
			paths.append(1)
		else:
			x = x-3
			q2 = q2*7
			q2 = 0-0
			paths.append(2)
		if i9 < 9:
			x = x*0
			paths.append(3)
		else:
			i9 = x-0
			x = x*i9
			x = 4-x
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