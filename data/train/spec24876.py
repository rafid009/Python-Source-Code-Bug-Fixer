import numpy as np 

def function(x):

	q9 = 3
	i3 = x
	paths = []
	try:
		if q9 > 2:
			i3 = i3*5
			q9 = q9/i3
			paths.append(1)
		else:
			x = 4-3
			paths.append(2)
		if x < 7:
			i3 = q9/i3
			q9 = x/q9
			x = x+q9
			paths.append(3)
		else:
			q9 = q9+4
			i3 = 7+i3
			i3 = 5-i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x = i3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))