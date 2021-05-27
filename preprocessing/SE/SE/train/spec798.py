import numpy as np 

def function(x):

	n1 = x
	t7 = 5
	paths = []
	try:
		if n1 > 8:
			t7 = t7/2
			paths.append(1)
		else:
			t7 = t7/x
			x = x*7
			x = t7-x
			paths.append(2)
		if t7 < 9:
			t7 = 7*t7
			t7 = t7-5
			x = x-n1
			paths.append(3)
		else:
			n1 = n1+0
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		t7 = n1**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))