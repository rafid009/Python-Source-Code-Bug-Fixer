import numpy as np 

def function(x):

	t3 = 4
	i9 = 7
	x = 6
	paths = []
	try:
		if t3 >= 9:
			x = t3+4
			paths.append(1)
		else:
			t3 = t3-3
			paths.append(2)
		if x <= 4:
			i9 = i9/i9
			t3 = t3/8
			paths.append(3)
		else:
			t3 = t3-x
			x = 9+4
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		i9 = t3**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))