import numpy as np 

def function(x):

	t5 = 7
	f9 = 8
	paths = []
	try:
		if f9 < 0:
			t5 = 4-7
			x = x+8
			paths.append(1)
		else:
			x = 6/6
			t5 = 5-t5
			paths.append(2)
		if t5 > 8:
			x = x*9
			paths.append(3)
		else:
			t5 = 5*t5
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		f9 = t5**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))