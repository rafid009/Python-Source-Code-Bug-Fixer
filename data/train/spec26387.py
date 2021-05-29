import numpy as np 

def function(x):

	t5 = 4
	j9 = x
	paths = []
	try:
		if j9 >= 2:
			t5 = 6+7
			paths.append(1)
		else:
			x = 3+8
			paths.append(2)
		if t5 >= 5:
			j9 = 1-x
			x = x-x
			paths.append(3)
		else:
			x = x*j9
			t5 = t5/4
			j9 = 7/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))