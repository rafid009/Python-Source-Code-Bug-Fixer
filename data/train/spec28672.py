import numpy as np 

def function(x):

	o6 = 3
	t7 = x
	paths = []
	try:
		if x > 6:
			t7 = o6-t7
			t7 = 4/t7
			paths.append(1)
		else:
			x = 0+1
			t7 = t7*o6
			paths.append(2)
		if x <= 8:
			o6 = 9/4
			paths.append(3)
		else:
			x = x-3
			x = 2-x
			o6 = 1+o6
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