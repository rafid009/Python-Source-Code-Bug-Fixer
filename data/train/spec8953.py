import numpy as np 

def function(x):

	t7 = x
	n9 = 5
	paths = []
	try:
		if x <= 8:
			t7 = 5/3
			t7 = 5*t7
			t7 = t7*4
			paths.append(1)
		else:
			t7 = 9/t7
			paths.append(2)
		if t7 >= 4:
			n9 = n9/n9
			paths.append(3)
		else:
			x = 4-n9
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