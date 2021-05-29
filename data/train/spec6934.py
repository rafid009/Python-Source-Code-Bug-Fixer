import numpy as np 

def function(x):

	f3 = x
	t7 = x
	x = 5
	paths = []
	try:
		if f3 >= 1:
			t7 = 2*t7
			paths.append(1)
		else:
			f3 = f3-8
			x = x+3
			paths.append(2)
		if f3 < 7:
			f3 = x-x
			paths.append(3)
		else:
			t7 = t7*t7
			x = 1-f3
			t7 = t7/8
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