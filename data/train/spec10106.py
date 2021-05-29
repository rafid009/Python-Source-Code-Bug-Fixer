import numpy as np 

def function(x):

	t6 = x
	y7 = x
	paths = []
	try:
		if t6 > 5:
			y7 = y7*4
			x = 4*6
			t6 = t6/4
			paths.append(1)
		else:
			y7 = x+0
			x = t6*x
			paths.append(2)
		if x <= 3:
			x = t6*2
			paths.append(3)
		else:
			t6 = x+y7
			t6 = t6+0
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))