import numpy as np 

def function(x):

	u7 = 1
	t9 = 6
	paths = []
	try:
		if t9 <= 9:
			t9 = x-t9
			x = 6/x
			paths.append(1)
		else:
			u7 = 3*7
			u7 = 3+u7
			paths.append(2)
		if u7 >= 6:
			x = x-t9
			paths.append(3)
		else:
			x = x*0
			x = 0-x
			t9 = t9/6
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))