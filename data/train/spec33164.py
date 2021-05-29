import numpy as np 

def function(x):

	t7 = 8
	o9 = x
	paths = []
	try:
		if o9 < 0:
			t7 = x-3
			paths.append(1)
		else:
			x = 5-x
			o9 = 9-o9
			paths.append(2)
		if t7 <= 6:
			x = x-7
			paths.append(3)
		else:
			o9 = 9/2
			x = x*x
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