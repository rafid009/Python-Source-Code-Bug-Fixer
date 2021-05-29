import numpy as np 

def function(x):

	a9 = 1
	t7 = 5
	paths = []
	try:
		if t7 >= 6:
			a9 = 6-a9
			paths.append(1)
		else:
			a9 = t7*1
			paths.append(2)
		if t7 >= 2:
			t7 = t7-8
			paths.append(3)
		else:
			x = x*a9
			x = x*7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))