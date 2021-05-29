import numpy as np 

def function(x):

	t4 = 3
	v7 = 6
	paths = []
	try:
		if t4 <= 6:
			t4 = x/v7
			v7 = 7*v7
			t4 = 9*t4
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if t4 < 7:
			v7 = v7/4
			x = v7/9
			paths.append(3)
		else:
			v7 = x*v7
			v7 = 1+v7
			v7 = t4-1
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))