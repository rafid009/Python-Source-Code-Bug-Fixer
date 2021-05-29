import numpy as np 

def function(x):

	n3 = x
	t7 = x
	paths = []
	try:
		if n3 > 9:
			n3 = x*x
			t7 = 9-t7
			x = x-5
			paths.append(1)
		else:
			t7 = n3/t7
			paths.append(2)
		if n3 <= 5:
			x = x*6
			paths.append(3)
		else:
			n3 = 0+x
			t7 = t7/t7
			t7 = 2-t7
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		t7 = n3**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))