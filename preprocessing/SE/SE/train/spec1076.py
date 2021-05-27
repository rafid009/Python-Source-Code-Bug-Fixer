import numpy as np 

def function(x):

	t6 = 9
	f8 = 1
	paths = []
	try:
		if f8 < 0:
			t6 = t6/9
			f8 = 8/t6
			f8 = f8+7
			paths.append(1)
		else:
			t6 = t6+x
			f8 = x+t6
			paths.append(2)
		if t6 > 3:
			x = x+t6
			paths.append(3)
		else:
			t6 = t6-t6
			f8 = t6*t6
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		t6 = f8**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))