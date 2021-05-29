import numpy as np 

def function(x):

	d7 = x
	t7 = 3
	paths = []
	try:
		if x >= 4:
			x = x+5
			t7 = t7/t7
			paths.append(1)
		else:
			x = x+t7
			d7 = d7+0
			d7 = d7/9
			paths.append(2)
		if x >= 4:
			t7 = 0+9
			paths.append(3)
		else:
			t7 = t7+7
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))