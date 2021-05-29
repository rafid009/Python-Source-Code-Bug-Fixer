import numpy as np 

def function(x):

	t7 = x
	f9 = x
	paths = []
	try:
		if f9 < 7:
			t7 = 6*8
			paths.append(1)
		else:
			t7 = f9*t7
			t7 = 0-3
			t7 = f9*t7
			paths.append(2)
		if x > 1:
			x = x+6
			t7 = 9-t7
			paths.append(3)
		else:
			x = t7*t7
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))