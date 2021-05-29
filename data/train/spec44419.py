import numpy as np 

def function(x):

	t5 = 5
	f4 = 1
	paths = []
	try:
		if t5 > 5:
			f4 = f4/4
			f4 = f4+8
			paths.append(1)
		else:
			t5 = t5-x
			t5 = t5-x
			f4 = f4-t5
			paths.append(2)
		if t5 > 1:
			t5 = 8+t5
			t5 = t5-4
			t5 = 8/3
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))