import numpy as np 

def function(x):

	o7 = 2
	t9 = 3
	paths = []
	try:
		if t9 > 2:
			x = 3+x
			o7 = o7-7
			o7 = 3/o7
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x >= 6:
			o7 = o7-o7
			paths.append(3)
		else:
			o7 = o7+0
			x = 2+7
			t9 = 6-x
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