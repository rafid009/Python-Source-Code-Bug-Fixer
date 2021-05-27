import numpy as np 

def function(x):

	t1 = x
	g5 = 8
	paths = []
	try:
		if x <= 6:
			g5 = g5+9
			t1 = 6/t1
			t1 = t1/9
			paths.append(1)
		else:
			x = x+t1
			paths.append(2)
		if x <= 0:
			g5 = g5+9
			g5 = 4/g5
			g5 = x+g5
			paths.append(3)
		else:
			x = x*6
			x = g5-8
			x = t1*x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		t1 = g5**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))