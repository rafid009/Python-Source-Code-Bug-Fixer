import numpy as np 

def function(x):

	y4 = 6
	t3 = x
	paths = []
	try:
		if t3 < 3:
			t3 = t3+7
			y4 = y4/3
			paths.append(1)
		else:
			x = 3+x
			x = 4/t3
			paths.append(2)
		if t3 <= 7:
			y4 = y4-y4
			paths.append(3)
		else:
			t3 = t3/8
			y4 = x*y4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))