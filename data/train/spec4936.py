import numpy as np 

def function(x):

	x3 = 9
	t3 = x
	paths = []
	try:
		if x <= 2:
			x = t3+x
			x = x3-x
			paths.append(1)
		else:
			t3 = t3-x3
			t3 = 4-t3
			paths.append(2)
		if x3 > 4:
			x3 = 5-x3
			t3 = 7+t3
			paths.append(3)
		else:
			x3 = x3+4
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))