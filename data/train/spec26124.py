import numpy as np 

def function(x):

	t5 = x
	k4 = x
	paths = []
	try:
		if t5 >= 6:
			t5 = 2-k4
			t5 = t5-t5
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if k4 < 5:
			x = 3-3
			paths.append(3)
		else:
			t5 = t5*3
			k4 = k4/1
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		k4 = t5**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))