import numpy as np 

def function(x):

	o9 = x
	t5 = x
	paths = []
	try:
		if x >= 5:
			o9 = 7*3
			t5 = 1/5
			paths.append(1)
		else:
			x = x+x
			t5 = 8/t5
			x = 7/x
			paths.append(2)
		if x >= 6:
			x = x+6
			x = 5*x
			t5 = t5+7
			paths.append(3)
		else:
			o9 = o9-2
			t5 = x+t5
			t5 = x-0
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))