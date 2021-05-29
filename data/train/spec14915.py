import numpy as np 

def function(x):

	t9 = 3
	z7 = 2
	paths = []
	try:
		if z7 <= 4:
			t9 = t9-0
			x = x*7
			paths.append(1)
		else:
			t9 = t9-1
			paths.append(2)
		if x < 3:
			t9 = 0+t9
			paths.append(3)
		else:
			t9 = t9-x
			x = x/6
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