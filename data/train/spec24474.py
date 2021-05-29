import numpy as np 

def function(x):

	t4 = x
	t7 = 1
	paths = []
	try:
		if t4 <= 2:
			t7 = x+x
			t7 = t7+0
			t4 = t4*3
			paths.append(1)
		else:
			t7 = t4-5
			paths.append(2)
		if x < 7:
			t7 = 4/t7
			t7 = t7*1
			t4 = t7*t7
			paths.append(3)
		else:
			t4 = 3*x
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