import numpy as np 

def function(x):

	i6 = 0
	t2 = x
	paths = []
	try:
		if i6 >= 4:
			x = x+4
			t2 = t2-6
			paths.append(1)
		else:
			i6 = x-4
			i6 = 3-x
			paths.append(2)
		if t2 > 8:
			i6 = 2/i6
			t2 = 1-t2
			x = 8+0
			paths.append(3)
		else:
			i6 = i6-4
			i6 = i6*t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		i6 = t2**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))