import numpy as np 

def function(x):

	i9 = 1
	t2 = 0
	x = 1
	paths = []
	try:
		if x > 2:
			i9 = i9/6
			x = 1-t2
			i9 = x+8
			paths.append(1)
		else:
			i9 = x*7
			i9 = i9*i9
			i9 = 4+7
			paths.append(2)
		if i9 > 5:
			i9 = 2-i9
			i9 = 2/i9
			t2 = t2/5
			paths.append(3)
		else:
			i9 = 3*5
			i9 = 8-x
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