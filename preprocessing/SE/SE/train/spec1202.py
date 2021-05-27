import numpy as np 

def function(x):

	f0 = x
	t4 = 9
	paths = []
	try:
		if f0 > 8:
			t4 = t4-f0
			f0 = 1-f0
			t4 = t4/2
			paths.append(1)
		else:
			t4 = 0-1
			paths.append(2)
		if t4 <= 3:
			f0 = f0/x
			paths.append(3)
		else:
			f0 = f0/t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))