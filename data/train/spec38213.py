import numpy as np 

def function(x):

	t5 = 5
	f4 = x
	paths = []
	try:
		if f4 >= 5:
			t5 = 5-0
			x = 5*x
			paths.append(1)
		else:
			t5 = x+4
			x = x*f4
			paths.append(2)
		if t5 <= 3:
			f4 = t5*f4
			paths.append(3)
		else:
			x = 5-7
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		t5 = f4**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))