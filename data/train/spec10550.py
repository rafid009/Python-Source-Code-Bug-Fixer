import numpy as np 

def function(x):

	t1 = x
	t7 = x
	paths = []
	try:
		if x > 5:
			t1 = x/9
			x = x/t7
			paths.append(1)
		else:
			x = t1+x
			t1 = x+x
			paths.append(2)
		if t7 >= 6:
			x = 5/x
			t7 = 3+t7
			paths.append(3)
		else:
			t7 = x-9
			t7 = t7/t7
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t7 = t1**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))