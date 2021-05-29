import numpy as np 

def function(x):

	i3 = 1
	q8 = x
	x = x
	paths = []
	try:
		if x >= 4:
			q8 = 7+3
			x = q8+5
			paths.append(1)
		else:
			x = 5+q8
			i3 = x-0
			q8 = 1-3
			paths.append(2)
		if q8 >= 9:
			i3 = 7*i3
			q8 = q8+0
			x = x*x
			paths.append(3)
		else:
			q8 = q8-8
			x = x-6
			q8 = 7*q8
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		q8 = i3**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))