import numpy as np 

def function(x):

	t5 = 8
	y6 = 5
	paths = []
	try:
		if y6 < 8:
			x = x+5
			paths.append(1)
		else:
			y6 = y6*x
			t5 = 8/t5
			paths.append(2)
		if x <= 5:
			t5 = 0/9
			paths.append(3)
		else:
			t5 = 2-8
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))