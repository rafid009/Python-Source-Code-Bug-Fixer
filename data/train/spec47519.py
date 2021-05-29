import numpy as np 

def function(x):

	t7 = 0
	a8 = x
	x = 2
	paths = []
	try:
		if x <= 2:
			x = 6-5
			t7 = 3-4
			t7 = t7/6
			paths.append(1)
		else:
			t7 = 3-4
			a8 = a8/7
			paths.append(2)
		if a8 <= 1:
			t7 = t7*4
			a8 = 2*4
			t7 = t7-8
			paths.append(3)
		else:
			a8 = 7-a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		t7 = a8**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))