import numpy as np 

def function(x):

	t7 = x
	b3 = x
	paths = []
	try:
		if t7 > 7:
			t7 = t7-b3
			paths.append(1)
		else:
			t7 = t7+b3
			t7 = 3-6
			paths.append(2)
		if x >= 0:
			x = x-6
			paths.append(3)
		else:
			b3 = 0+b3
			b3 = 6/t7
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