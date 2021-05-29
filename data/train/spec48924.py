import numpy as np 

def function(x):

	t7 = 1
	f4 = 3
	paths = []
	try:
		if x <= 5:
			f4 = 3+f4
			paths.append(1)
		else:
			t7 = 0/f4
			t7 = 1-t7
			paths.append(2)
		if x < 4:
			x = x/3
			t7 = t7+9
			t7 = 1-f4
			paths.append(3)
		else:
			t7 = 7+0
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