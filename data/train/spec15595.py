import numpy as np 

def function(x):

	t4 = x
	t7 = 9
	paths = []
	try:
		if t7 > 7:
			x = x+0
			x = x-7
			t4 = t4*2
			paths.append(1)
		else:
			t7 = t4-t4
			t7 = t7/x
			paths.append(2)
		if t4 < 7:
			x = 7+x
			t4 = t4-0
			paths.append(3)
		else:
			t4 = 8/4
			t4 = t4+t7
			t7 = 7+t7
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))