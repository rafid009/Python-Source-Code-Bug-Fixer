import numpy as np 

def function(x):

	t4 = x
	i0 = 1
	paths = []
	try:
		if t4 >= 5:
			x = x+3
			x = 5-i0
			i0 = 6-9
			paths.append(1)
		else:
			i0 = i0*3
			paths.append(2)
		if i0 >= 4:
			x = 6*x
			t4 = 5-t4
			paths.append(3)
		else:
			x = 9/9
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		t4 = i0**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))