import numpy as np 

def function(x):

	i7 = 4
	t2 = 7
	paths = []
	try:
		if x <= 7:
			x = x+7
			paths.append(1)
		else:
			t2 = t2*4
			i7 = i7-i7
			paths.append(2)
		if x >= 6:
			i7 = 8-5
			paths.append(3)
		else:
			i7 = 8+i7
			t2 = 9/t2
			t2 = 3/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))